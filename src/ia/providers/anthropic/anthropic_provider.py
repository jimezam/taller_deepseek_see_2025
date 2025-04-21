from src.ia.providers.provider import Provider
import anthropic
from openai import OpenAI

class AnthropicProvider(Provider):
    def __init__(self):
        super().__init__()

    def get_provider_name(self):
        return "ANTHROPIC"

    def get_min_temperature(self) -> float:
        return 0.0

    def get_max_temperature(self) -> float:
        return 1.0

    def get_client(self) -> anthropic:
        print(self.get_config("API_KEY"))
        return anthropic.Anthropic(
            api_key=self.get_config("API_KEY")
        )

    def make_request(self, client: OpenAI, context: str, question: str) -> object:
        return client.messages.create(
            model=self.get_config("MODEL"),
            system=context,
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": question},
                ]},
            ],
            stream=False,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

    def get_response_text(self, response: object) -> str:
        return response.content[0].text
