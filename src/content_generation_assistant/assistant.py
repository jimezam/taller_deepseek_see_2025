from src.ia.providers.provider import Provider
from src.content_generation_assistant.content_type import ContentType

class Assistant:

    @classmethod
    def generate(cls, provider: Provider, content_type: ContentType, prompt: str) -> str:

        try:
            provider.temperature = content_type.get_preferred_temperature()
        except ValueError as e:
            raise ValueError(f"Invalid temperature value: {e} for {provider.get_provider_name()} range is ({provider.get_min_temperature()}, {provider.get_max_temperature()})")

        return provider.query(content_type.get_context(), prompt)



# - c'odigo fuente
# - post para facebook
# - guion para tiktok
