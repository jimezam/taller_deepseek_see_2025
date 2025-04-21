from src.ia.providers.provider import Provider
from src.ia.providers.deepseek.deepseek_provider import DeepSeekProvider
from src.ia.providers.mistral.mistral_provider import MistralProvider
from src.ia.providers.anthropic.anthropic_provider import AnthropicProvider
from src.content_generation_assistant.assistant import Assistant
from src.content_generation_assistant.content_types.personal_cover_letter import PersonalCoverLetter
from src.content_generation_assistant.content_types.source_code import SourceCode

def main():
    provider:Provider = DeepSeekProvider()
    # provider:Provider = MistralProvider()
    # provider:Provider = AnthropicProvider()

    prompt: str = """
        Crea un programa en Rust que le pida al usuario los siguientes valores:
        valor de la cuenta del restaurante, valor del impuesto, porcentaje de propina
        y cantidad de personas. El programa debe mostrar el valor total de la cuenta real,
        el valor total de la cuenta con el impuesto y el valor que le corresponde pagar
        a cada persona.
    """

    text: str = Assistant.generate(
        provider,
        SourceCode(),
        prompt
    )

    print(text)


if __name__ == "__main__":
    main()



# def main():
#     # provider:Provider = DeepSeekProvider()
#     # provider:Provider = MistralProvider()
#     # provider:Provider = AnthropicProvider()

#     context = "This is a test context."
#     question = "What is the meaning of life?"

#     try:
#         response = provider.query(context, question)
#         print("Response:", response)
#     except ValueError as e:
#         print(e)


    # prompt: str = """
    #     Mi nombre es Jorge Iván, soy ingeniero de sistemas y me gusta desarrollar software,
    #     dormir, molestar gatitos, ir al cine y comer repollos. He trabajado en varias empresas,
    #     tanto como desarrollador como docente de ingeniería a nivel de pregrado y posgrado.
    #     Me interesa trabajar en esta empresa porque considero que puedo contribuir de manera valiosa
    #     en el proceso de renovación tecnológica en el que se encuentran. Además, me gusta que me paguen mucho y ojalá no tenga
    #     que hacer mucho porque siempre tengo sueño. Sin embargo, las pocas horas en que estoy
    #     despierto soy un prolífico desarrollador que crea código limpio basado en patrones y
    #     buenas prácticas de software.
    # """