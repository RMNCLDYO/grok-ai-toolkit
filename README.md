<p align="center">
    <a href="https://x.ai/" title="Go to xAI homepage">
        <img src="https://img.shields.io/badge/Grok%20by%20xAI-000000?style=for-the-badge&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMjkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogMi4xLjAgQnVpbGQgMTg2KSAgLS0+CiAgPGRlZnM+CiAgICA8c3R5bGU+CiAgICAgIC5zdDAgewogICAgICAgIGZpbGw6ICNmZmY7CiAgICAgIH0KICAgIDwvc3R5bGU+CiAgPC9kZWZzPgogIDxnIGlkPSJMYXllcl8xIiBmb2N1c2FibGU9ImZhbHNlIj4KICAgIDxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0xLjYsOC42bDEwLjQsMTQuOWg0LjZMNi4zLDguNkgxLjZaTTYuMywxNi45bC00LjYsNi42aDQuNmwyLjMtMy4zLTIuMy0zLjNaTTE3LjcuNWwtOCwxMS40LDIuMywzLjNMMjIuNC41aC00LjZaTTE4LjYsNy42djE1LjloMy44VjIuMmwtMy44LDUuNFoiLz4KICA8L2c+Cjwvc3ZnPg==" alt="Grok by xAI">
    </a>
</p>

<p align="center">
    <a href="https://github.com/RMNCLDYO/grok-ai-toolkit" title="Go to repo">
        <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=Grok+AI+Toolkit&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2Fgrok-ai-toolkit%2Fmain%2F.github%2Fversion.json" alt="Grok AI Toolkit">
    </a>
</p>

<p align="center">
    <a href=".github/CHANGELOG.md" title="Go to changelog"><img src="https://img.shields.io/badge/maintained-yes-2ea44f?style=for-the-badge" alt="maintained - yes"></a>
    <a href=".github/CONTRIBUTING.md" title="Go to contributions doc"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f?style=for-the-badge" alt="contributions - welcome"></a>
</p>

<p align="center">
    <a href="/">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RMNCLDYO/grok-ai-toolkit/main/.github/xAI-logo-dark.png">
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RMNCLDYO/grok-ai-toolkit/main/.github/xAI-logo-light.png">
          <img alt="xAI" width="250" src="https://raw.githubusercontent.com/RMNCLDYO/grok-ai-toolkit/main/.github/xAI-logo-dark.png">
        </picture>
    </a>
</p>

A powerful Python-based API wrapper and command-line interface for interacting with xAI's Grok language models. This toolkit provides seamless integration with xAI's Grok language models for chat, text completion, and vision analysis capabilities.

## 🚀 Features

- 🤖 Interactive chat sessions with Grok by xAI language models
- 📝 Single-shot text completion
- 👁️ Vision analysis with support for local images and URLs
- ⚡ Real-time streaming responses
- 🎯 Configurable model parameters
- 🔄 Conversation history management
- 📤 File upload handling for images
- ⚙️ Extensive parameter validation
- 🎨 Beautiful loading animations

## 📋 Table of Contents

- [Installation](#-installation)
- [API Key Configuration](#-configuration)
- [Usage](#-usage)
- [Special Commands](#-special-commands)
- [Advanced Configuration](#%EF%B8%8F-advanced-configuration)
- [Supported Models](#-supported-models)
- [Error Handling and Safety](#-error-handling-and-safety)
- [Supported File Types](#-supported-file-types)
- [Caching and Cleanup](#-caching-and-cleanup)
- [Contributing](#-contributing)
- [Issues and Support](#-issues-and-support)
- [Feature Requests](#-feature-requests)
- [Versioning and Changelog](#-versioning-and-changelog)
- [Security](#-security)
- [License](#-license)

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RMNCLDYO/grok-ai-toolkit.git
   ```

2. Navigate to the repository folder:
   ```bash
   cd grok-ai-toolkit
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configuration
1. Obtain an API key from [xAI](https://console.x.ai/).
2. You have three options for managing your API key:
   <details>
   <summary>Click here to view the API key configuration options</summary>
   
   - **Setting it as an environment variable on your device (recommended for everyday use)**
       - Navigate to your terminal.
       - Add your API key like so:
         ```shell
         export GROK_API_KEY=your_api_key
         ```
       This method allows the API key to be loaded automatically when using the wrapper or CLI.
     
   - **Using an .env file (recommended for development):**
       - Install python-dotenv if you haven't already: `pip install python-dotenv`.
       - Create a .env file in the project's root directory.
       - Add your API key to the .env file like so:
         ```makefile
         GROK_API_KEY=your_api_key
         ```
       This method allows the API key to be loaded automatically when using the wrapper or CLI.
     
   - **Direct Input:**
       - If you prefer not to use a `.env` file, you can directly pass your API key as an argument to the CLI or the wrapper functions.
         
         ***CLI***
         ```shell
         --api_key "your_api_key"
         ```
         ***Wrapper***
         ```shell
         api_key="your_api_key"
         ```
       This method requires manually inputting your API key each time you initiate an API call.
   </details>

## 💻 Usage

### Text Mode
*For generating text based on a prompt or a set of instructions.*

***CLI***
```bash
python cli.py --text --prompt "Write a story about AI."
```

***Wrapper***
```python
from grok import Text

Text().run(prompt="Write a story about AI.")
```

### Chat Mode
*For interactive conversations with the AI model.*

***CLI***
```bash
python cli.py --chat
```

***Wrapper***
```python
from grok import Chat

Chat().run()
```

### Vision Mode
*For processing images alongside text, allowing for visual analysis and multimodal interactions. This mode enables you to upload images (from local paths or URLs) and chat with the AI about their content.*

***CLI***
```bash
python cli.py --vision --prompt "What's in this image?" --image_path image.jpg
```

***Wrapper***
```python
from grok import Vision

Vision().run(prompt="What's in this image?", image_path="image.jpg")
```

## 🔧 Special Commands
During interaction with the toolkit, you can use the following special commands:

- `/exit` or `/quit`: End the conversation and exit the program.
- `/clear`: Clear the conversation history.
- `/upload`: (Vision mode only) Upload an image for analysis. 
   - Usage: `/upload file_path_or_url [optional prompt]`
   - Example: `/upload image.jpg What do you see in this image?`

## ⚙️ Advanced Configuration

| Description | CLI Flags | CLI Usage | Wrapper Usage |
|-------------|-----------|-----------|---------------|
| Chat mode | `-c`, `--chat` | `--chat` | *See mode usage above.* |
| Text mode | `-t`, `--text` | `--text` | *See mode usage above.* |
| Vision mode | `-v`, `--vision` | `--vision` | *See mode usage above.* |
| User prompt | `-p`, `--prompt` | `--prompt "Your prompt here"` | `prompt="Your prompt here"` |
| Image path | `-ip`, `--image_path` | `--image_path "image.jpg"` | `image_path="image.jpg"` |
| Image URL | `-iu`, `--image_url` | `--image_url "https://example.com/image.jpg"` | `image_url="https://example.com/image.jpg"` |
| Enable streaming | `-s`, `--stream` | `--stream` | `stream=True` |
| API Key | `-ak`, `--api_key` | `--api_key "your_api_key"` | `api_key="your_api_key"` |
| Model name | `-m`, `--model` | `--model "model_name"` | `model="model_name"` |
| System prompt | `-sp`, `--system_prompt` | `--system_prompt "Set custom instructions"` | `system_prompt="Set custom instructions"` |
| Max tokens | `-mt`, `--max_tokens` | `--max_tokens 1024` | `max_tokens=1024` |
| Temperature | `-tm`, `--temperature` | `--temperature 0.7` | `temperature=0.7` |
| Top-p | `-tp`, `--top_p` | `--top_p 0.9` | `top_p=0.9` |
| Top-k | `-tk`, `--top_k` | `--top_k 40` | `top_k=40` |
| Frequency penalty | `-fp`, `--frequency_penalty` | `--frequency_penalty 0.5` | `frequency_penalty=0.5` |
| Presence penalty | `-pp`, `--presence_penalty` | `--presence_penalty 0.5` | `presence_penalty=0.5` |
| Number of completions | `-n` | `--n 1` | `n=1` |
| Stop sequences | `-stop`, `--stop_sequences` | `--stop_sequences [".", "\n"]` | `stop=[".", "\n"]` |

## 📊 Supported Models

| Model | Input | Output | Context ( Max Tokens) |
|-------|--------|---------|-----------------|
| grok-2-vision-1212 | Image, Text | Text | 8192 |
| grok-2-1212 | Text | Text | 131072 |
| grok-vision-beta | Image, Text | Text | 8192 |
| grok-beta | Text | Text | 131072 |

*The `grok-2` and `grok-2-latest` model names are aliased to the latest chat models, currently `grok-2-1212`. You can use `grok-2` and `grok-2-latest` if you want to automatically access the latest model version, or choose a model with a specific version number to keep a consistent output.*

> [!NOTE]
> Note your model access might vary depending on various factors such as geographical location, account limitations, etc. For the most up-to-date information on your team's model access, visit the API Models page on your xAI [Console Models Page](https://console.x.ai/team/default/models).

## 🔒 Error Handling and Safety

The Grok AI Toolkit includes robust error handling to help you diagnose and resolve issues quickly. Here are some common error codes and their solutions:

| HTTP Code | Status | Description | Solution |
|-----------|--------|-------------|----------|
| 400 | Bad Request | Malformed request or invalid parameters | Check request format and parameters |
| 401 | Unauthorized | Invalid or missing API key | Verify your API key |
| 403 | Forbidden | Insufficient permissions | Check API key permissions |
| 404 | Not Found | Resource not found | Verify endpoint and model availability |
| 429 | Too Many Requests | Rate limit exceeded | Reduce request frequency |
| 500 | Internal Server Error | Server-side error | Retry after a short wait |
| 503 | Service Unavailable | Service temporarily down | Retry after a short wait |

## 📁 Supported File Types

The Grok AI Toolkit supports the following image formats for vision processing:

| Category | File Extensions |
|----------|----------------|
| **Images** | `jpg`, `jpeg`, `png`, `gif`, `webp`, `bmp` |

> [!WARNING]
> xAI has a limit of 10MB for file uploads.

## 💾 Caching and Cleanup

The Grok AI Toolkit implements a caching mechanism for uploaded images to improve performance and reduce unnecessary network requests:

1. When an image is uploaded from a URL, it's stored in a temporary cache folder (`.grok_ai_toolkit_cache`).
2. The cache is automatically cleaned up at the end of each session.
3. Cached files are managed efficiently to prevent storage bloat.

The caching system is automated and requires no manual management.

## 🤝 Contributing
Contributions are welcome!

Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

## 🐛 Issues and Support
Encountered a bug? We'd love to hear about it. Please follow these steps to report any issues:

1. Check if the issue has already been reported.
2. Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to create a detailed report.
3. Submit the report [here](https://github.com/RMNCLDYO/grok-ai-toolkit/issues).

Your report will help us make the project better for everyone.

## 💡 Feature Requests
Got an idea for a new feature? Feel free to suggest it. Here's how:

1. Check if the feature has already been suggested or implemented.
2. Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to create a detailed request.
3. Submit the request [here](https://github.com/RMNCLDYO/grok-ai-toolkit/issues).

Your suggestions for improvements are always welcome.

## 🔁 Versioning and Changelog
Stay up-to-date with the latest changes and improvements in each version:

- [CHANGELOG.md](.github/CHANGELOG.md) provides detailed descriptions of each release.

## 🔐 Security
Your security is important to us. If you discover a security vulnerability, please follow our responsible disclosure guidelines found in [SECURITY.md](.github/SECURITY.md). Please refrain from disclosing any vulnerabilities publicly until said vulnerability has been reported and addressed.

## 📄 License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.