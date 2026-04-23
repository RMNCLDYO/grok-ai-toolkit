# Grok AI Toolkit

> **Unmaintained.** Use [`xai-sdk`](https://github.com/xai-org/xai-sdk-python), xAI's official Python SDK.

I've always preferred pair programming with LLMs from the terminal over copy-pasting from browser chats. Web UIs hit rate limits, lose context across tabs, and break flow when I'm moving code back and forth. When xAI opened Grok to developers in October 2024, there was no first-party Python SDK yet. I wanted chat/text/vision modes, local-image uploads with URL fallback, streaming, and the full parameter surface (temperature, top_p, top_k, frequency/presence penalty) behind one CLI. So I built this for myself.

Python wrapper and CLI for xAI's Grok models, including vision.

## Install

```bash
git clone https://github.com/ramonclaudio/grok-ai-toolkit.git
cd grok-ai-toolkit
pip install -r requirements.txt
```

## Configuration

Get an API key at https://console.x.ai/. Set via env var, `.env`, or pass directly:

```bash
export GROK_API_KEY=your_api_key
```

## CLI

```bash
# Chat
python cli.py --chat

# Text
python cli.py --text --prompt "Write a story about AI."

# Vision from local path
python cli.py --vision --prompt "What's in this image?" --image_path "/path/to/image.jpg"

# Vision from URL
python cli.py --vision --prompt "What's in this image?" --image_url "https://example.com/image.jpg"
```

## Python

```python
from grok import Chat, Text, Vision

Chat().run()
Text().run(prompt="Write a story about AI.")
Vision().run(prompt="What's in this image?", image_path="/path/to/image.jpg")
Vision().run(prompt="What's in this image?", image_url="https://example.com/image.jpg")
```

## In-session commands

- `/exit` or `/quit`: end the session
- `/clear`: clear conversation history
- `/upload`: (vision mode) `/upload file_path_or_url [optional prompt]`

## Options

| Description | CLI | Python |
| --- | --- | --- |
| Chat mode | `--chat` | `Chat()` |
| Text mode | `--text` | `Text()` |
| Vision mode | `--vision` | `Vision()` |
| Prompt | `--prompt` | `prompt=` |
| Image path | `--image_path` | `image_path=` |
| Image URL | `--image_url` | `image_url=` |
| Streaming | `--stream` | `stream=True` |
| API key | `--api_key` | `api_key=` |
| Model | `--model` | `model=` |
| System prompt | `--system_prompt` | `system_prompt=` |
| Max tokens | `--max_tokens` | `max_tokens=` |
| Temperature | `--temperature` | `temperature=` |
| Top-p | `--top_p` | `top_p=` |
| Top-k | `--top_k` | `top_k=` |
| Frequency penalty | `--frequency_penalty` | `frequency_penalty=` |
| Presence penalty | `--presence_penalty` | `presence_penalty=` |
| Completions | `--n` | `n=` |
| Stop sequences | `--stop_sequences` | `stop=` |

## Models

| Model | Input | Output | Max tokens |
| --- | --- | --- | --- |
| `grok-2-vision-1212` | image, text | text | 8192 |
| `grok-2-1212` | text | text | 131072 |
| `grok-vision-beta` | image, text | text | 8192 |
| `grok-beta` | text | text | 131072 |

`grok-2` and `grok-2-latest` alias to the latest chat model. Pin a version number for reproducibility.

## File support

Vision supports `jpg`, `jpeg`, `png`, `gif`, `webp`, `bmp`. 10MB upload limit per xAI.

## Caching

URL-uploaded images cache to `.grok_ai_toolkit_cache` and clear on session end.

## Errors

| Code | Meaning | Fix |
| --- | --- | --- |
| 400 | Bad request | Check params |
| 401 | Unauthorized | Verify API key |
| 403 | Forbidden | Check key permissions |
| 404 | Not found | Verify endpoint / model access |
| 429 | Rate limited | Back off |
| 500 | Server error | Retry |
| 503 | Service down | Retry |

## License

MIT
