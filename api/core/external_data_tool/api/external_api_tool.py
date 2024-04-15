from typing import Dict, Optional

import requests
from core.external_data_tool.base import ExternalDataTool


class ExternalAPITool(ExternalDataTool):
    name: str = "external_api"

    @classmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        required_keys = ["api_endpoint", "api_key"]
        for key in required_keys:
            if key not in config or not config[key]:
                raise ValueError(f"{key} is required in the configuration")

    def query(self, inputs: dict, query: Optional[str] = None) -> str:
        api_endpoint = self.config.get("api_endpoint")
        api_key = self.config.get("api_key")
        request_method = self.config.get("request_method", "GET").upper()
        headers = {"Authorization": f"Bearer {api_key}"}

        try:
            if request_method == "GET":
                response = requests.get(api_endpoint, params=inputs, headers=headers)
            elif request_method == "POST":
                response = requests.post(api_endpoint, json=inputs, headers=headers)
            else:
                raise ValueError(f"Unsupported request method: {request_method}")

            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")

        try:
            response_data = response.json()
        except ValueError:
            raise ValueError("Failed to parse response JSON")

        if 'result' not in response_data:
            raise ValueError("API response does not contain 'result' field")

        return response_data['result']
