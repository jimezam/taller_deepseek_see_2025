from src.ia.providers.provider import Provider
from mistralai import Mistral
from openai import OpenAI

class MistralProvider(Provider):
    def __init__(self):
        super().__init__()

    def get_provider_name(self):
        return "MISTRAL"

    def get_min_temperature(self) -> float:
        return 0.0

    def get_max_temperature(self) -> float:
        return 2.0

    def get_client(self) -> OpenAI:
        return Mistral(
            api_key=self.get_config("API_KEY")
        )

    def make_request(self, client: OpenAI, context: str, question: str) -> object:
        return client.chat.complete(
            model=self.get_config("MODEL"),
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": question},

                # {"role": "user", "content": [
                #     {"type": "text", "text": "hello"},
                #     {"type": "document_url", "document_url": "https://example.com"},
                # ]},
            ],
            stream=False,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

    def get_response_text(self, response: object) -> str:
        return response.choices[0].message.content
