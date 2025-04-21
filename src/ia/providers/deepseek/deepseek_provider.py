from src.ia.providers.provider import Provider
from openai import OpenAI


class DeepSeekProvider(Provider):
    def __init__(self, config):
        super().__init__(config)

    def get_provider_name(self):
        return "DEEPSEEK"

    def get_min_temperature(self) -> float:
        return 0.0

    def get_max_temperature(self) -> float:
        return 1.0

    def get_client(self) -> OpenAI:
        return OpenAI(
            api_key=self.get_config("API_KEY"),
            base_url=self.get_config("BASE_URL")
        )

    def make_request(self, client: OpenAI, context: str, question: str) -> object:
        return client.chat.completions.create(
            model=self.get_config("MODEL"),
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": question},
            ],
            stream=False,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

    def get_response_text(self, response: object) -> str:
        return response.choices[0].message.content
