import requests

class ExternalContext:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        try:
            response = requests.get(self.base_url + endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error occurred: {err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def post(self, endpoint, data=None):
        try:
            response = requests.post(self.base_url + endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error occurred: {err}')
        except Exception as err:
            print(f'Other error occurred: {err}')