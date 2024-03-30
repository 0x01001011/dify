from typing import Optional

import requests
from core.external_data_tool.base import ExternalDataTool


class ExternalAPITool(ExternalDataTool):
    name: str = "external_api"

    @classmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        if "api_endpoint" not in config or "api_key" not in config:
            raise ValueError("Configuration must include 'api_endpoint' and 'api_key'.")

    def query(self, inputs: dict, query: Optional[str] = None) -> str:
        api_endpoint = self.config.get("api_endpoint")
        api_key = self.config.get("api_key")
        headers = {"Authorization": f"Bearer {api_key}"}

        try:
            response = requests.get(api_endpoint, headers=headers, params=inputs)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Failed to query external API: {e}")

        try:
            return response.json()
        except ValueError:
            raise ValueError("Invalid response format from external API.")
