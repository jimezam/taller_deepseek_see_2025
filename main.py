from src.ia.providers.provider import Provider
from src.ia.providers.deepseek.deepseek_provider import DeepSeekProvider
from src.ia.providers.mistral.mistral_provider import MistralProvider
from src.ia.providers.anthropic.anthropic_provider import AnthropicProvider
from src.content_generation_assistant.assistant import Assistant
from src.content_generation_assistant.content_types.personal_cover_letter import PersonalCoverLetter
from src.content_generation_assistant.content_types.source_code import SourceCode
from src.content_generation_assistant.content_types.tiktok_script import TiktokScript
from src.content_generation_assistant.content_types.short_love_poem import ShortLovePoem
from src.ui import show

def main():
    show()

    # provider:Provider = DeepSeekProvider()
    # provider:Provider = MistralProvider()
    # provider:Provider = AnthropicProvider()

    # prompt: str = """
    #     Nombre de mi novia: Vaca Neria
    #     Ella es muy pequeñita, amable, baila como si tuviera dos pies izquierdos pero tiene ojos bonitos.
    #     Cuando sonríe, el sol brilla. Casi nunca lo hace, por eso llueve tanto.
    #     Nos gusta programar juntos hasta el amanecer, en silencio, porque cuando calla parece como ausente.
    #     La quiero mucho, que nunca cambie, que no me olvide.
    #     Tono preferido: poético.
    # """

    # text: str = Assistant.generate(
    #     provider,
    #     ShortLovePoem(),
    #     prompt
    # )

    # print(text)


if __name__ == "__main__":
    main()