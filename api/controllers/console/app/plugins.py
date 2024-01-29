from langchain.openai_utils import OpenAICompletion
from langchain.prompts import Prompt
from requests import RequestException, get


class ExternalAPIPlugin:
    def __init__(self, api_url=None):
        self.api_url = api_url
        self.openai_completion = OpenAICompletion()

    def set_api_url(self, url):
        self.api_url = url

    def make_request(self):
        if not self.api_url:
            raise ValueError("API URL is not configured.")
        try:
            response = get(self.api_url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise ConnectionError(f"Failed to make request to external API: {e}")

    def process_response(self, response_data):
        if not isinstance(response_data, dict):
            raise ValueError("Response data is not a valid JSON object.")
        prompt = Prompt(response_data)
        completion = self.openai_completion.complete(prompt)
        return completion

    def generate_prompt(self):
        response_data = self.make_request()
        return self.process_response(response_data)
