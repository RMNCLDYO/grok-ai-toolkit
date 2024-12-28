import os
import sys
import shutil
import base64
import mimetypes
from urllib.parse import urlparse

class FileHandler:
    def __init__(self, api_key, directory_path):
        self.api_key = api_key
        self.directory_path = directory_path
        self.cache_folder_path = os.path.join(directory_path, 'grok_ai_toolkit_cache')
        os.makedirs(self.cache_folder_path, exist_ok=True)

    def handle_upload_command(self, user_input, detail="high"):
        new_files, new_prompt = self.parse_upload_command(user_input)
        if new_files:
            processed_new_files = self.process_files(new_files, detail)
            return processed_new_files, new_prompt
        else:
            print("[ ERROR ]: No valid files were provided with the upload command.")
            print("[ ERROR ]: Please check your file paths and try again.")
            return None, None

    def process_files(self, files, detail="high"):
        processed_files = []
        for file in files:
            file_info = self.process_file(file, detail)
            if file_info:
                processed_files.append(file_info)
        
        if not processed_files:
            print("[ ERROR ]: No valid files were processed.")
            return None
        
        return processed_files

    def process_file(self, file_input, detail="high"):
        if self.is_valid_url(file_input):
            return self.process_url_file(file_input, detail)
        elif os.path.isfile(file_input):
            return self.process_local_file(file_input, detail)
        else:
            print(f"[ ERROR ]: Invalid file input: {file_input}")
            sys.exit(1)

    def process_local_file(self, file_path, detail="high"):
        try:
            mime_type = self.get_mime_type(file_path)
            if not mime_type:
                return None

            file_size = os.path.getsize(file_path)
            if file_size > 10 * 1024 * 1024:
                print(f"[ ERROR ]: File size exceeds 10MiB limit: {file_path}")
                return None

            with open(file_path, 'rb') as f:
                file_data = f.read()
                base64_data = base64.b64encode(file_data).decode('utf-8')
                return {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime_type};base64,{base64_data}",
                        "detail": detail
                    }
                }
        except Exception as e:
            print(f"[ ERROR ]: Failed to process local file: {str(e)}")
            sys.exit(1)

    def process_url_file(self, url, detail="high"):
        try:
            return {
                "type": "image_url",
                "image_url": {
                    "url": url,
                    "detail": detail
                }
            }
        except Exception as e:
            print(f"[ ERROR ]: Failed to process URL: {str(e)}")
            sys.exit(1)

    def cleanup_cache(self):
        try:
            if os.path.exists(self.cache_folder_path):
                shutil.rmtree(self.cache_folder_path)
                print("\n[ SUCCESS ]: Cache folder cleaned.")
            os.makedirs(self.cache_folder_path, exist_ok=True)
        except Exception as e:
            print(f"[ ERROR ]: Failed to clean cache: {str(e)}")
            sys.exit(1)

    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            sys.exit(1)

    def get_mime_type(self, file_path):
        mime_type, _ = mimetypes.guess_type(file_path)
        if not mime_type or not mime_type.startswith('image/'):
            print(f"[ ERROR ]: Unsupported file type: {file_path}")
            sys.exit(1)
        return mime_type

    def parse_upload_command(self, user_input):
        parts = user_input.split()
        if len(parts) < 2:
            print("[ ERROR ]: Please provide file path(s) after the /upload command.")
            return [], None
        
        files = []
        prompt = ""
        for part in parts[1:]:
            if os.path.exists(part) or self.is_valid_url(part):
                files.append(part)
            else:
                prompt = " ".join(parts[parts.index(part):])
                break
        
        return files, prompt if prompt else None