from typing import Optional

from core.extension.api_based_extension_requestor import APIBasedExtensionRequestor
from core.external_data_tool.base import ExternalDataTool
from core.helper import encrypter
from extensions.ext_database import db
from models.api_based_extension import APIBasedExtension, APIBasedExtensionPoint


class ApiExternalDataTool(ExternalDataTool):
    """
    The api external data tool.
    """

    name: str = "api"
    """the unique name of external data tool"""

    @classmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        """
        Validate the incoming form config data.

        :param tenant_id: the id of workspace
        :param config: the form config data
        :return:
        """
        # own validation logic
        api_based_extension_id = config.get("api_based_extension_id")
        if not api_based_extension_id:
            raise ValueError("api_based_extension_id is required")

        # get api_based_extension
        api_based_extension = db.session.query(APIBasedExtension).filter(
            APIBasedExtension.tenant_id == tenant_id,
            APIBasedExtension.id == api_based_extension_id
        ).first()

    def retrieve_external_data(self, api_endpoint: str, headers: Optional[dict] = None) -> dict:
        """
        Retrieve data from the configured API URL.

        :param api_endpoint: The API endpoint to make the request to.
        :param headers: Optional headers for the request.
        :return: The response data as a dictionary.
        """
        # Implementation of API request logic using requests library
        import requests
        try:
            response = requests.get(api_endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f'Failed to retrieve data from {api_endpoint}: {e}')
        

        if not api_based_extension:
            raise ValueError("api_based_extension_id is invalid")

    def query(self, inputs: dict, query: Optional[str] = None) -> str:
        """
        Query the external data tool.

        :param inputs: user inputs
        :param query: the query of chat app
        :return: the tool query result
        """
        # Retrieve data using the new method
        api_endpoint = self.config.get('api_endpoint')
        headers = self.config.get('headers', None)
        response_data = self.retrieve_external_data(api_endpoint, headers)

        # Process the response data to customize the prompt
        # This is a placeholder for processing logic, potentially integrating with LangChain and OpenAI
        customized_prompt = 'Customized prompt based on response data: ' + str(response_data)

        # Original code for reference
        # get params from config
        api_based_extension_id = self.config.get("api_based_extension_id")

        # get api_based_extension
        api_based_extension = db.session.query(APIBasedExtension).filter(
            APIBasedExtension.tenant_id == self.tenant_id,
            APIBasedExtension.id == api_based_extension_id
        ).first()

        if not api_based_extension:
            raise ValueError("[External data tool] API query failed, variable: {}, "
                             "error: api_based_extension_id is invalid"
                             .format(self.variable))

        # decrypt api_key
        api_key = encrypter.decrypt_token(
            tenant_id=self.tenant_id,
            token=api_based_extension.api_key
        )

        try:
            # request api
            requestor = APIBasedExtensionRequestor(
                api_endpoint=api_based_extension.api_endpoint,
                api_key=api_key
            )
        except Exception as e:
            raise ValueError("[External data tool] API query failed, variable: {}, error: {}".format(
                self.variable,
                e
            ))

        response_json = requestor.request(point=APIBasedExtensionPoint.APP_EXTERNAL_DATA_TOOL_QUERY, params={
            'app_id': self.app_id,
            'tool_variable': self.variable,
            'inputs': inputs,
            'query': query
        })

        if 'result' not in response_json:
            raise ValueError("[External data tool] API query failed, variable: {}, error: result not found in response"
                             .format(self.variable))

        if not isinstance(response_json['result'], str):
            raise ValueError("[External data tool] API query failed, variable: {}, error: result is not string"
                             .format(self.variable))

        return response_json['result']
