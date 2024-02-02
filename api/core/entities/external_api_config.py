from typing import Dict, Optional


class ExternalAPIConfig:
    def __init__(self, url: str, method: str, params: Optional[Dict[str, str]] = None, data: Optional[Dict[str, Any]] = None) -> None:
        self.url = url
        self.method = method
        self.params = params
        self.data = data
