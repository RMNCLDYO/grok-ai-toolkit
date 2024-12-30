import sys
import argparse
from grok import Chat, Text, Vision

def main():
    parser = argparse.ArgumentParser(
        description="""
    ------------------------------------------------------------------
                             Grok AI Toolkit                             
                   API Wrapper & Command-line Interface               
                          [v1.1.0] by @rmncldyo                       
    ------------------------------------------------------------------

    Grok AI toolkit is an API wrapper and command-line interface for xAI's Grok language models.

    Modes:
    - Chat: Interactive conversation with the model
    - Text: Single prompt-response interaction
    - Vision: Image analysis and multimodal interaction

    For detailed usage information, visit: github.com/rmncldyo/grok-ai-toolkit
    """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-c', '--chat', action='store_true', help='Start an interactive chat session')
    mode_group.add_argument('-t', '--text', action='store_true', help='Generate a single text response')
    mode_group.add_argument('-v', '--vision', action='store_true', help='Enable vision mode for image analysis')

    parser.add_argument('-ak', '--api_key', type=str, help='Your Grok API key')
    parser.add_argument('-m', '--model', type=str, help='Specify which model to use')
    parser.add_argument('-p', '--prompt', type=str, help='The text prompt to send')
    parser.add_argument('-sp', '--system_prompt', type=str, help='Set system-level instructions')
    parser.add_argument('-s', '--stream', action='store_true', help='Enable streaming mode for responses')
    parser.add_argument('-mt', '--max_tokens', type=int, help='Maximum tokens in response')
    parser.add_argument('-tm', '--temperature', type=float, help='Response randomness (0.0 to 2.0)')
    parser.add_argument('-tp', '--top_p', type=float, help='Response diversity (0.0 to 1.0)')
    parser.add_argument('-tk', '--top_k', type=int, help='Top K token filtering')
    parser.add_argument('-fp', '--frequency_penalty', type=float, help='Frequency penalty (-2.0 to 2.0)')
    parser.add_argument('-pp', '--presence_penalty', type=float, help='Presence penalty (-2.0 to 2.0)')
    parser.add_argument('-n', type=int, help='Number of completions to generate')
    parser.add_argument('-sd', '--seed', type=int, help='Seed for generation')
    parser.add_argument('-u', '--user', type=str, help='User for generation')
    parser.add_argument('-ip', '--image_path', type=str, help='Path to local image file')
    parser.add_argument('-iu', '--image_url', type=str, help='URL of image to analyze')
    parser.add_argument('-stop', '--stop_sequences', nargs='+', help='Sequences that stop generation')

    try:
        args = parser.parse_args()
    except SystemExit:
        print("[ ERROR ]: Invalid command-line arguments. Please check the usage and try again.")
        sys.exit(1)

    common_args = {
        'api_key': args.api_key,
        'model': args.model,
        'prompt': args.prompt,
        'system_prompt': args.system_prompt,
        'stream': args.stream,
        'max_tokens': args.max_tokens,
        'temperature': args.temperature,
        'top_p': args.top_p,
        'top_k': args.top_k,
        'frequency_penalty': args.frequency_penalty,
        'presence_penalty': args.presence_penalty,
        'n': args.n,
        'seed': args.seed,
        'user': args.user,
        'stop': args.stop_sequences
    }

    try:
        if args.chat:
            Chat().run(**common_args)
        elif args.text:
            Text().run(**common_args)
        elif args.vision:
            Vision().run(
                image_path=args.image_path,
                image_url=args.image_url,
                **common_args
            )
    except Exception as e:
        print(f"[ ERROR ]: An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()