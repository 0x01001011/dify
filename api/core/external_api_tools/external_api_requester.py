import json

import requests
from requests.exceptions import HTTPError, RequestException


class ExternalAPIRequester:
    def __init__(self, api_endpoint, headers=None, params=None, data=None):
        self.api_endpoint = api_endpoint
        self.headers = headers if headers is not None else {}
        self.params = params if params is not None else {}
        self.data = data if data is not None else {}

    def get(self):
        try:
            response = requests.get(self.api_endpoint, headers=self.headers, params=self.params)
            return self._parse_response(response)
        except RequestException as e:
            raise Exception(self._handle_request_exception(e))

    def post(self):
        try:
            response = requests.post(self.api_endpoint, headers=self.headers, params=self.params, json=self.data)
            return self._parse_response(response)
        except RequestException as e:
            raise Exception(self._handle_request_exception(e))

    def _parse_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            error_msg = f'HTTP error occurred: {http_err}'
            raise Exception(error_msg)
        except ValueError as json_err:
            error_msg = f'Response content is not valid JSON: {json_err}'
            raise Exception(error_msg)

    def _handle_request_exception(self, exception):
        if isinstance(exception, HTTPError):
            return f'HTTP error: {exception.response.status_code} {exception.response.reason}'
        elif isinstance(exception, RequestException):
            return f'Request exception: {exception}'
        else:
            return 'An unexpected error occurred'
