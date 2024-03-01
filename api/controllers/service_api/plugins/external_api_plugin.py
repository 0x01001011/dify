import json

import requests
from langchain import LangChain


class ExternalAPIPlugin:
    def __init__(self):
        self.api_url = None
        self.langchain = LangChain()

    def set_api_url(self, url):
        self.api_url = url

    def make_request(self, method='GET', data=None, params=None):
        if method.upper() == 'POST':
            response = requests.post(self.api_url, json=data)
        else:
            response = requests.get(self.api_url, params=params)
        response.raise_for_status()
        return response.json()

    def process_response(self, response):
        processed_data = self.langchain.process(response)
        return processed_data
