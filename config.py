import os
import sys
from dotenv import load_dotenv

def load_config(api_key=None):
    try:
        if not api_key:
            api_key = load_required_env_variables('XAI_API_KEY')
        
        if not api_key:
            print("[ ERROR ]: Failed to load API key. Please ensure it's set in your environment variables or .env file.")
            print("You can set it by running: export XAI_API_KEY=your_api_key_here")
            sys.exit(1)

        config = {
            'api_key': api_key,
            'base_model': os.getenv('XAI_BASE_MODEL', 'grok-beta'),
            'vision_model': os.getenv('XAI_VISION_MODEL', 'grok-2v-mini'),
            'base_url': os.getenv('XAI_BASE_URL', 'https://api.x.ai'),
            'api_version': os.getenv('XAI_API_VERSION', 'v1')
        }

        if not validate_config(config):
            print("[ ERROR ]: Invalid configuration. Please check your environment variables and try again.")
            sys.exit(1)

        return config
    except Exception as e:
        print(f"[ ERROR ]: An unexpected error occurred while loading configuration: {str(e)}")
        print("Please ensure all required environment variables are set correctly.")
        sys.exit(1)

def load_required_env_variables(var_name):
    value = os.getenv(var_name)
    if value is None:
        try:
            load_dotenv()
            value = os.getenv(var_name)
            if not value:
                print(f"[ ERROR ]: {var_name} environment variable is not defined.")
                sys.exit(1)
        except ImportError:
            print("[ ERROR ]: dotenv package is not installed. Please install it with 'pip install python-dotenv' or define the environment variables directly.")
            sys.exit(1)
        except Exception as e:
            print(f"[ ERROR ]: Encountered an error loading environment variables: {str(e)}")
            sys.exit(1)
    return value

def validate_config(config):
    required_keys = ['api_key', 'base_model']
    for key in required_keys:
        if key not in config or not config[key]:
            print(f"[ ERROR ]: Missing or empty required configuration: {key}")
            sys.exit(1)

    if not config['api_key'].strip():
        print("[ ERROR ]: API key is empty or consists only of whitespace")
        sys.exit(1)
    
    if not config['base_model'].strip():
        print("[ ERROR ]: Model is empty or consists only of whitespace")
        sys.exit(1)

    return True