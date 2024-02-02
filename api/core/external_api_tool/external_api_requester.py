import requests


class ExternalAPIRequester:
    @staticmethod
    def get_data_from_api(url: str, params: dict) -> dict:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {'error': f'HTTP error occurred: {http_err}'}
        except requests.exceptions.ConnectionError as conn_err:
            return {'error': f'Connection error occurred: {conn_err}'}
        except requests.exceptions.Timeout as timeout_err:
            return {'error': 'The request timed out'}
        except requests.exceptions.RequestException as req_err:
            return {'error': f'An error occurred: {req_err}'}

    @staticmethod
    def post_data_to_api(url: str, data: dict) -> dict:
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {'error': f'HTTP error occurred: {http_err}'}
        except requests.exceptions.ConnectionError as conn_err:
            return {'error': f'Connection error occurred: {conn_err}'}
        except requests.exceptions.Timeout as timeout_err:
            return {'error': 'The request timed out'}
        except requests.exceptions.RequestException as req_err:
            return {'error': f'An error occurred: {req_err}'}
