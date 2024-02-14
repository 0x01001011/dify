import json

import requests
from langchain import LangChain
from openai import OpenAI


class ExternalAPIPlugin:
    def __init__(self, api_url=""):
        self.api_url = api_url
        self.langchain = LangChain()
        self.openai = OpenAI()

    def set_api_url(self, url):
        self.api_url = url

    def make_request(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def process_response(self, response):
        if "error" in response:
            return {"error": response["error"]}
        prompt = self.langchain.generate_prompt(response)
        return self.openai.complete(prompt)
