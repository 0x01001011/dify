from typing import Any, Dict, Optional

import requests
from core.external_data_tool.base import ExternalDataTool
from core.helper import encrypter
from extensions.ext_database import db
from models.api_based_extension import APIBasedExtension


class ExternalAPIPlugin(ExternalDataTool):
    name: str = "external_api"

    def __init__(self):
        self.api_url: Optional[str] = None
        self.params: Dict[str, Any] = {}

    def configure(self, api_url: str, params: Optional[Dict[str, Any]] = None) -> None:
        self.api_url = api_url
        if params is not None:
            self.params = params

    def make_request(self) -> Dict[str, Any]:
        if not self.api_url:
            raise ValueError("API URL is not configured.")
        response = requests.get(self.api_url, params=self.params)
        response.raise_for_status()
        return response.json()

    def customize_prompt_with_langchain_and_openai(self, data: Dict[str, Any]) -> str:
        # Integration with LangChain and OpenAI to generate a creative response based on the data
        formatted_data = ', '.join([f'{key}: {value}' for key, value in data.items()])
        prompt = f"Here's the data: {formatted_data}\nCan you generate a creative response based on this?"
        # Assuming `langchain_client` is an instance of a LangChain client configured elsewhere
        response = langchain_client.generate(prompt=prompt, model="text-davinci-003")
        return response['choices'][0]['text']

    @classmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        api_based_extension_id = config.get("api_based_extension_id")
        if not api_based_extension_id:
            raise ValueError("api_based_extension_id is required")
        api_based_extension = db.session.query(APIBasedExtension).filter(
            APIBasedExtension.tenant_id == tenant_id,
            APIBasedExtension.id == api_based_extension_id
        ).first()
        if not api_based_extension:
            raise ValueError("api_based_extension_id is invalid")
