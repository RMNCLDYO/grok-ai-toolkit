import os
import sys
from client import Client
from validators import InputValidator
from file_handler import FileHandler

class GrokBase:
    def __init__(self):
        self.client = None
        self.model = None
        self.input_validator = InputValidator()
        self.directory_path = os.path.dirname(__file__)
        self.file_handler = None
        self.conversation_history = []

    def handle_user_input(self, user_input, mode):
        if user_input.lower() in ['exit', 'quit', '/exit', '/quit']:
            return "exit", None, None

        if user_input.lower() == '/clear':
            return "clear", None, None

        if mode == "vision" and user_input.startswith('/upload'):
            print()
            processed_files, user_text = self.file_handler.handle_upload_command(user_input)
            return "upload", processed_files, user_text

        return None, None, user_input

    def prepare_conversation_data(self, conversation_history, system_prompt=None, max_tokens=None, 
                                temperature=None, top_p=None, top_k=None, frequency_penalty=None, presence_penalty=None, 
                                n=None, stop=None, stream=None, seed=None, user=None):
        try:
            payload = {
                "messages": conversation_history,
                "model": self.model
            }

            if not self.input_validator.validate_max_tokens(max_tokens):
                return None

            if not self.input_validator.validate_temperature(temperature):
                return None
            
            if not self.input_validator.validate_top_p(top_p):
                return None

            if not self.input_validator.validate_top_k(top_k):
                return None

            if not self.input_validator.validate_frequency_penalty(frequency_penalty):
                return None

            if not self.input_validator.validate_presence_penalty(presence_penalty):
                return None
            
            if not self.input_validator.validate_n(n):
                return None
            
            if not self.input_validator.validate_stop_sequences(stop):
                return None
            
            if not self.input_validator.validate_stream(stream):
                return None
            
            if not self.input_validator.validate_seed(seed):
                return None
            
            if not self.input_validator.validate_user(user):
                return None

            generation_config = {
                "temperature": float(temperature) if temperature is not None else None,
                "top_p": float(top_p) if top_p is not None else None,
                "top_k": int(top_k) if top_k is not None else None,
                "max_tokens": int(max_tokens) if max_tokens is not None else None,
                "frequency_penalty": float(frequency_penalty) if frequency_penalty is not None else None,
                "presence_penalty": float(presence_penalty) if presence_penalty is not None else None,
                "n": int(n) if n is not None else None,
                "stop": stop if stop else None,
                "stream": bool(stream) if stream is not None else None,
                "seed": int(seed) if seed is not None else None,
                "user": user if user else None
            }

            generation_config = {k: v for k, v in generation_config.items() if v is not None}
            if generation_config:
                payload.update(generation_config)

            if system_prompt:
                system_message = {
                    "role": "system",
                    "content": system_prompt
                }
                conversation_history.insert(0, system_message)

            return payload
            
        except Exception as e:
            print(f"[ ERROR ]: Failed to prepare conversation data: {str(e)}")
            sys.exit(1)

    def initialize_client(self, api_key, model, mode):
        try:
            self.client = Client(api_key=api_key)
            self.model = model if model else (self.client.config.get('vision_model') if mode == "vision" else self.client.config.get('base_model'))
            if mode == "vision":
                self.file_handler = FileHandler(self.client.api_key, self.directory_path)
        except Exception as e:
            print(f"[ ERROR ]: Failed to initialize client: {str(e)}")
            sys.exit(1)