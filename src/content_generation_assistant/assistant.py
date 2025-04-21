from src.ia.providers.provider import Provider
from src.content_generation_assistant.content_type import ContentType

class Assistant:

    @classmethod
    def generate(cls, provider: Provider, content_type: ContentType, prompt: str) -> str:
        # SET TEMPERATURE

        print(provider.temperature)
        provider.temperature = content_type.get_preferred_temperature()
        print(provider.temperature)

        return provider.query(content_type.get_context(), prompt)


# ia.provider
# type de contenido
# - carta de presentaci'on
# - c'odigo fuente
# - post para facebook
# - guion para tiktok
