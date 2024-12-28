import sys
from base import GrokBase

class Text(GrokBase):
    def run(self, api_key=None, model=None, prompt=None, stream=None, system_prompt=None, 
            max_tokens=None, temperature=None, top_p=None, top_k=None,
            frequency_penalty=None, presence_penalty=None, n=None, stop=None, seed=None, user=None):
        mode = "text"
        try:
            self.initialize_client(api_key, model, mode)

            if not self.input_validator.validate_text_input(prompt):
                return

            command, _, text = self.handle_user_input(prompt, mode)
            if command == "exit":
                return

            self.conversation_history.append({"role": "user", "content": text})

            conversation_data = self.prepare_conversation_data(
                self.conversation_history, system_prompt,
                max_tokens, temperature, top_p, top_k,
                frequency_penalty, presence_penalty, n, stop, stream, seed, user
            )
            
            if conversation_data is None:
                print("[ ERROR ]: Failed to prepare conversation data")
                return

            print("User: " + text)
            response = self.client.send_message(conversation_data, stream=stream)
            if response:
                self.conversation_history.append({"role": "assistant", "content": response.strip()})
                if not stream:
                    print(f"Assistant: {response.strip()}")
            else:
                print("[ ERROR ]: No response received from the assistant.")

        except Exception as e:
            print(f"[ ERROR ]: An unexpected error occurred: {str(e)}")
            sys.exit(1)
        finally:
            print("\nThank you for using the Grok AI toolkit. Have a great day!")

class Chat(GrokBase):
    def run(self, api_key=None, model=None, prompt=None, stream=None, system_prompt=None, 
            max_tokens=None, temperature=None, top_p=None, top_k=None,
            frequency_penalty=None, presence_penalty=None, n=None, stop=None, seed=None, user=None):
        mode = "chat"
        try:
            self.initialize_client(api_key, model, mode)
            
            print("\nEnter '/clear' at any time to clear the conversation history.")
            print("Enter '/exit' or '/quit' at any time to end the conversation.\n")
            
            print("Assistant: Hello! How can I assist you today?")
            while True:
                try:
                    if prompt:
                        user_input = prompt.strip()
                        print(f"User: {user_input}")
                        prompt = None
                    else:
                        user_input = input("User: ").strip()

                    command, _, text = self.handle_user_input(user_input, mode)
                    if command == "exit":
                        break
                    elif command == "clear":
                        self.conversation_history = []
                        print("Assistant: Conversation history has been cleared.")
                        continue

                    if not text:
                        print("[ ERROR ]: Invalid input detected. Please enter a valid message.")
                        continue

                    self.conversation_history.append({"role": "user", "content": text})

                    conversation_data = self.prepare_conversation_data(
                        self.conversation_history, system_prompt, max_tokens, 
                        temperature, top_p, top_k, frequency_penalty, presence_penalty, n, stop, stream, seed, user
                    )

                    if conversation_data is None:
                        print("[ ERROR ]: Failed to prepare conversation data")
                        continue

                    response = self.client.send_message(conversation_data, stream=stream)
                    
                    if response:
                        self.conversation_history.append({"role": "assistant", "content": response.strip()})
                        if not stream:
                            print(f"Assistant: {response.strip()}")
                    else:
                        print("[ ERROR ]: No response received from the assistant.")
                
                except Exception as e:
                    print(f"[ ERROR ]: An unexpected error occurred: {str(e)}")
                    
        except Exception as e:
            print(f"[ ERROR ]: An unexpected error occurred: {str(e)}")
            sys.exit(1)
        finally:
            print("\nThank you for using the Grok AI toolkit. Have a great day!")

class Vision(GrokBase):
    def run(self, api_key=None, model=None, prompt=None, image_path=None, image_url=None,
            stream=None, system_prompt=None, max_tokens=None, temperature=None, 
            top_p=None, top_k=None, frequency_penalty=None, presence_penalty=None, 
            n=None, stop=None, image_detail=None, seed=None, user=None):
        mode = "vision"
        try:
            self.initialize_client(api_key, model, mode)
            
            print("\nEnter '/upload' at any time followed by the image path or URL and an optional prompt.")
            print("Example: /upload /path/to/image.jpg What's in this image?")
            print("\nEnter '/clear' to clear conversation history.")
            print("Enter '/exit' or '/quit' to end the conversation.\n")
            
            if image_path or image_url:
                files = [image_path] if image_path else [image_url]
                processed_files = self.file_handler.process_files(files, image_detail or "high")
                if processed_files:
                    message_content = []
                    for file_info in processed_files:
                        message_content.append(file_info)
                    if prompt:
                        message_content.append({"type": "text", "text": prompt})
                    self.conversation_history.append({"role": "user", "content": message_content})
            
            if not image_path and not image_url:
                print("Assistant: Hello! I'm ready to analyze any images you'd like to share.")

            while True:
                try:
                    if self.conversation_history and self.conversation_history[-1]["role"] == "user":
                        conversation_data = self.prepare_conversation_data(
                            self.conversation_history, system_prompt, max_tokens, 
                            temperature, top_p, top_k, frequency_penalty, presence_penalty, n, stop, stream, seed, user
                        )

                        if conversation_data is None:
                            print("[ ERROR ]: Failed to prepare conversation data")
                            continue

                        response = self.client.send_message(conversation_data, stream=stream)

                        if response:
                            self.conversation_history.append({"role": "assistant", "content": response.strip()})
                            if not stream:
                                print(f"Assistant: {response.strip()}")
                        else:
                            print("[ ERROR ]: No response received from the assistant.")

                    user_input = input("User: ").strip()
                    
                    command, processed_files, text = self.handle_user_input(user_input, mode, image_detail)
                    
                    if command == "exit":
                        break
                    elif command == "clear":
                        self.conversation_history = []
                        print("Assistant: Conversation history has been cleared.")
                        continue
                    elif command == "upload":
                        if not processed_files:
                            continue
                            
                        message_content = []
                        for file_info in processed_files:
                            message_content.append(file_info)
                        if text:
                            message_content.append({"type": "text", "text": text})
                        self.conversation_history.append({"role": "user", "content": message_content})
                    elif text:
                        self.conversation_history.append({"role": "user", "content": [{"type": "text", "text": text}]})
                    else:
                        print("[ ERROR ]: Invalid input detected. Please enter a valid message or use the /upload command.")
                        continue

                except Exception as e:
                    print(f"[ ERROR ]: An unexpected error occurred: {str(e)}")
                    sys.exit(1)

        except Exception as e:
            print(f"[ ERROR ]: An unexpected error occurred: {str(e)}")
            sys.exit(1)
        finally:
            if self.file_handler:
                self.file_handler.cleanup_cache()
            print("\nThank you for using the Grok AI toolkit. Have a great day!")