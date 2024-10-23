import sys
import json
import requests
from config import load_config
from loading import Loading

class Client:
    def __init__(self, api_key=None):
        try:
            self.config = load_config(api_key=api_key)
            self.api_key = api_key or self.config.get('api_key')
            self.base_url = self.config.get('base_url')
            self.model = self.config.get('base_model')
            self.api_version = self.config.get('api_version')
            self.headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            self.loading = Loading()
        except Exception as e:
            print(f"[ ERROR ]: Failed to initialize Client: {str(e)}")
            sys.exit(1)

    def get(self, endpoint=None, headers=None):
        try:
            response = self._make_request('GET', endpoint=endpoint, headers=headers)
            if response:
                return response.json()
            return None
        except Exception as e:
            print(f"[ ERROR ]: GET request failed: {str(e)}")
            sys.exit(1)

    def post(self, endpoint=None, data=None, headers=None, stream=None):
        try:
            response = self._make_request('POST', endpoint=endpoint, data=data, headers=headers, stream=stream)
            if response:
                if stream:
                    return response
                return self._handle_response(response.json())
            return None
        except Exception as e:
            print(f"[ ERROR ]: POST request failed: {str(e)}")
            sys.exit(1)

    def send_message(self, conversation_data=None, stream=None):
        try:
            endpoint = 'chat/completions'
            if stream:
                return self._handle_stream(endpoint, conversation_data)
            return self.post(endpoint, conversation_data)
        except Exception as e:
            print(f"[ ERROR ]: Failed to send message: {str(e)}")
            sys.exit(1)

    def _make_request(self, method=None, endpoint=None, data=None, headers=None, stream=None):
        url = f"{self.base_url}/{self.api_version}/{endpoint}"
        request_headers = self.headers
        if headers:
            request_headers.update(headers)

        try:
            if not stream:
                self.loading.start()
            response = requests.request(
                method=method,
                url=url,
                headers=request_headers,
                json=data,
                stream=stream,
                timeout=60
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            self._handle_request_errors(e)
            return None
        finally:
            if not stream:
                self.loading.stop()

    def _handle_stream(self, endpoint, data):
        try:
            response = self.post(endpoint, data, stream=True)
            if not response:
                return None

            print("Assistant: ", end='', flush=True)
            content = ''

            for line in response.iter_lines():
                if not line:
                    continue

                line = line.decode('utf-8')
                if line.startswith('data: '):
                    line = line[6:]
                    if line == '[DONE]':
                        break

                    try:
                        json_data = json.loads(line)
                        choice = json_data.get('choices', [{}])[0]
                        delta = choice.get('delta', {})
                        content_chunk = delta.get('content', '')
                        
                        if content_chunk:
                            print(content_chunk, end='', flush=True)
                            content += content_chunk

                    except json.JSONDecodeError:
                        continue

            print()
            return content.strip() if content else None

        except Exception as e:
            print(f"\n[ ERROR ]: Stream failed: {str(e)}")
            sys.exit(1)

    def _handle_request_errors(self, error=None):
        if isinstance(error, requests.exceptions.HTTPError):
            status_code = error.response.status_code
            try:
                error_data = error.response.json()
                message = error_data.get('error', {}).get('message', '')
            except:
                message = str(error)

            error_info = self._get_error_info(status_code, message)
            print(f"[ ERROR ]: {error_info}")
            sys.exit(1)
        elif isinstance(error, requests.exceptions.Timeout):
            print("[ ERROR ]: Request timed out. Please check your network connection and try again.")
            sys.exit(1)
        elif isinstance(error, requests.exceptions.ConnectionError):
            print("[ ERROR ]: Connection error. Please check your internet connection and try again.")
            sys.exit(1)
        else:
            print(f"[ ERROR ]: An unexpected error occurred: {str(error)}")
            sys.exit(1)

    def _get_error_info(self, status_code=None, message=None):
        error_map = {
            400: "Bad request. Please check your request parameters.",
            401: "Authentication failed. Please check your API key.",
            403: "Permission denied. Please check your API key permissions.",
            404: "Resource not found. Please check your request URL.",
            429: "Too many requests. Please slow down your request rate.",
            500: "Server error. Please try again later.",
            503: "Service unavailable. Please try again later."
        }
        return f"{error_map.get(status_code, 'Unknown error')}: {message}"

    def _handle_response(self, response_data=None):
        try:
            if "error" in response_data:
                error_message = response_data["error"].get("message", "Unknown API error")
                print(f"[ ERROR ]: API Error: {error_message}")
                sys.exit(1)

            choices = response_data.get("choices", [])
            if not choices:
                print("[ ERROR ]: No response choices received")
                return None

            choice = choices[0]
            message = choice.get("message", {})
            content = message.get("content", "")

            return content.strip()

        except Exception as e:
            print(f"[ ERROR ]: Failed to handle response: {str(e)}")
            sys.exit(1)