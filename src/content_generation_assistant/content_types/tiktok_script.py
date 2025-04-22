from src.content_generation_assistant.content_type import ContentType
from src.ia.providers.provider import Provider

class TiktokScript(ContentType):
    def __init__(self):
        super().__init__()

    def get_id(self) -> str:
        return "content_types.tiktok_script"

    def get_name(self) -> str:
        return "Guion para TikTok"

    def get_description(self) -> str:
        return "Genera un guion para TikTok que sea atractivo y divertido, con un enfoque en la creatividad y la originalidad. El guion debe ser breve y directo, ideal para el formato de TikTok, y debe incluir elementos visuales y auditivos que lo hagan más interesante. El contenido debe ser apropiado para la audiencia de TikTok y seguir las tendencias actuales de la plataforma."

    def get_example(self) -> str:
        return """
        """

    def get_context(self) -> str:
        return """
            A partir de la informacion ingresada por el usuario, crea un guion breve,
            divertido y altamente creativo para un video de TikTok. El guion debe
            captar la atención en los primeros 3 segundos, tener un giro inesperado
            o humorístico, y durar entre 15 y 30 segundos. Usa un tono casual y
            original. Incluye sugerencias de efectos visuales, sonidos virales o
            música de tendencia, y elementos que fomenten la interacción
            (como preguntas o llamadas a la acción). El contenido debe ser apropiado
            para la audiencia de TikTok (adolescentes y jóvenes adultos) y alineado
            con las tendencias actuales de la plataforma.
        """

    def get_preferred_temperature(self) -> float:
        return 0.8
        # return Provider.MAX_TEMPERATURE