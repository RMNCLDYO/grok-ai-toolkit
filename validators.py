import os
import sys
import json
import mimetypes

class InputValidator:
    def __init__(self):
        self.supported_image_types = {
            'image/jpeg', 'image/jpg', 'image/png', 
            'image/gif', 'image/webp', 'image/bmp'
        }
        self.max_file_size = 20 * 1024 * 1024  # 20MB
        
    def validate_text_input(self, prompt):
        if not prompt or not isinstance(prompt, str):
            print("[ ERROR ]: Invalid input. Please provide a valid text prompt.")
            sys.exit(1)
        return True

    def validate_temperature(self, temp):
        if temp is not None and not 0 <= float(temp) <= 2:
            print("[ ERROR ]: Temperature must be between 0 and 2")
            sys.exit(1)
        return True
    
    def validate_max_tokens(self, max_tokens):
        if max_tokens is not None and not isinstance(max_tokens, int):
            print("[ ERROR ]: Max tokens must be an integer")
            sys.exit(1)
        return True

    def validate_top_p(self, top_p):
        if top_p is not None and not 0 <= float(top_p) <= 1:
            print("[ ERROR ]: Top P must be between 0 and 1")
            sys.exit(1)
        return True
    
    def validate_top_k(self, top_k):
        if top_k is not None and not isinstance(top_k, int):
            print("[ ERROR ]: Top K must be an integer")
            sys.exit(1)
        return True
    
    def validate_stream(self, stream):
        if stream is not None and not isinstance(stream, bool):
            print("[ ERROR ]: Stream must be a boolean")
            sys.exit(1)
        return True

    def validate_frequency_penalty(self, penalty):
        if penalty is not None and not -2 <= float(penalty) <= 2:
            print("[ ERROR ]: Frequency penalty must be between -2 and 2")
            sys.exit(1)
        return True

    def validate_presence_penalty(self, penalty):
        if penalty is not None and not -2 <= float(penalty) <= 2:
            print("[ ERROR ]: Presence penalty must be between -2 and 2")
            sys.exit(1)
        return True

    def validate_n(self, n):
        if n is not None and (not isinstance(n, int) or n < 1):
            print("[ ERROR ]: n must be a positive integer")
            sys.exit(1)
        return True

    def validate_stop_sequences(self, sequences):
        if sequences is not None:
            if not isinstance(sequences, list):
                print("[ ERROR ]: Stop sequences must be a list")
                sys.exit(1)
            if len(sequences) > 4:
                print("[ ERROR ]: Maximum of 4 stop sequences allowed")
                sys.exit(1)
            if not all(isinstance(s, str) for s in sequences):
                print("[ ERROR ]: All stop sequences must be strings")
                sys.exit(1)
        return True

    def validate_image(self, image_path):
        if not os.path.exists(image_path):
            print(f"[ ERROR ]: Image file not found: {image_path}")
            sys.exit(1)
        
        if not os.access(image_path, os.R_OK):
            print(f"[ ERROR ]: Cannot read image file: {image_path}")
            sys.exit(1)
        
        if os.path.getsize(image_path) > self.max_file_size:
            print(f"[ ERROR ]: Image file too large (max {self.max_file_size/(1024*1024)}MB)")
            sys.exit(1)
        
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type or mime_type not in self.supported_image_types:
            print(f"[ ERROR ]: Unsupported image type: {mime_type}")
            sys.exit(1)
        
        return True

    def validate_image_url(self, url):
        if not url:
            print("[ ERROR ]: Image URL cannot be empty")
            sys.exit(1)
        
        if not url.startswith(('http://', 'https://', 'data:image/')):
            print("[ ERROR ]: Invalid image URL format")
            sys.exit(1)
        
        return True

    def validate_json(self, data):
        try:
            if isinstance(data, str):
                json.loads(data)
            return True
        except json.JSONDecodeError:
            print("[ ERROR ]: Invalid JSON format")
            sys.exit(1)
        
    def validate_seed(self, seed):
        if seed is not None and not isinstance(seed, int):
            print("[ ERROR ]: Seed must be an integer")
            sys.exit(1)
        return True
    
    def validate_user(self, user):
        if user is not None and not isinstance(user, str):
            print("[ ERROR ]: User must be a string")
            sys.exit(1)
        return True