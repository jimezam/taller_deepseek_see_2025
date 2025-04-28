from src.ia.providers.provider import Provider
from src.content_generation_assistant.content_type import ContentType
from src.ia.providers.anthropic.anthropic_provider import AnthropicProvider
from src.ia.providers.deepseek.deepseek_provider import DeepSeekProvider
from src.ia.providers.mistral.mistral_provider import MistralProvider
from src.content_generation_assistant.content_types.personal_cover_letter import PersonalCoverLetter
from src.content_generation_assistant.content_types.short_love_poem import ShortLovePoem
from src.content_generation_assistant.content_types.source_code import SourceCode
from src.content_generation_assistant.content_types.tiktok_script import TiktokScript

class Assistant:

    @staticmethod
    def get_provider_list() -> list:
        return [DeepSeekProvider,
                MistralProvider,
                AnthropicProvider]

    @staticmethod
    def get_content_types() -> list:
        return [PersonalCoverLetter,
                SourceCode,
                TiktokScript,
                ShortLovePoem]

    @classmethod
    def generate(cls, provider: Provider, content_type: ContentType, prompt: str) -> str:

        try:
            provider.temperature = provider.get_max_temperature() if content_type.get_preferred_temperature() == Provider.MAX_TEMPERATURE else content_type.get_preferred_temperature()
        except ValueError as e:
            raise ValueError(f"Invalid temperature value: {e} for {provider.get_provider_name()} range is ({provider.get_min_temperature()}, {provider.get_max_temperature()})")

        return provider.query(content_type.get_context(), prompt)