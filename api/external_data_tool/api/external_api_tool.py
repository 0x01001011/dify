import requests


class ExternalApiTool:
    def fetch_data(self, url: str, params: dict) -> dict:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch data: {str(e)}"}
        except ValueError:
            return {"error": "Invalid response format"}
