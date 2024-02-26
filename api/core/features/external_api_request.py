from typing import Any, Dict, Optional

import requests


class ExternalAPIRequestFeature:
    def configure_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        return {
            "endpoint": endpoint,
            "params": params if params else {},
            "headers": headers if headers else {}
        }

    def make_request(self, request_config: Dict[str, Any]) -> requests.Response:
        method = request_config.get("method", "GET")
        if method.upper() == "GET":
            response = requests.get(request_config["endpoint"], params=request_config.get("params", {}), headers=request_config.get("headers", {}))
        elif method.upper() == "POST":
            response = requests.post(request_config["endpoint"], json=request_config.get("params", {}), headers=request_config.get("headers", {}))
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        return response

    def parse_response(self, response: requests.Response) -> Any:
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
