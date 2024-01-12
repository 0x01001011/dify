import json

import requests


class ExternalAPIPlugin:
    def __init__(self):
        self.api_url = None
        self.api_response = None

    def set_api_url(self, api_url):
        self.api_url = api_url

    def make_api_request(self):
        response = requests.get(self.api_url)
        self.api_response = json.loads(response.text)

    def customize_prompt(self):
        # This is a placeholder implementation. The actual implementation will depend on the structure of the API response and the requirements of the prompt.
        return "Customized prompt based on API response: " + str(self.api_response)
