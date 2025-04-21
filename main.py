from src.ia.providers.provider import Provider
from src.ia.providers.deepseek.deepseek_provider import DeepSeekProvider
from src.ia.providers.mistral.mistral_provider import MistralProvider
from src.ia.providers.anthropic.anthropic_provider import AnthropicProvider

def main():
    # provider:Provider = DeepSeekProvider(config={})
    # provider:Provider = MistralProvider(config={})
    # provider:Provider = AnthropicProvider(config={})

    context = "This is a test context."
    question = "What is the meaning of life?"

    try:
        response = provider.query(context, question)
        print("Response:", response)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
