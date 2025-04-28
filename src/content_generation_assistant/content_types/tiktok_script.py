from src.content_generation_assistant.content_type import ContentType

class TiktokScript(ContentType):
    def __init__(self):
        super().__init__()

    def get_id(self) -> str:
        return "content_types.tiktok_script"

    def get_name(self) -> str:
        return "Guion para TikTok"

    def get_description(self) -> str:
        return "Genera un guion para TikTok que sea atractivo, divertido y que las tendencias actuales de la plataforma"

    def get_example(self) -> str:
        return """Un creador de contenido de programación llamado Alex, conocido por 
su humor sarcástico y su estilo único, quiere promocionar un producto llamado 
"GlowSnack", una barra de energía que brilla en la oscuridad. La finalidad del video 
es entretener y generar curiosidad sobre el producto, mientras se mantiene el tono 
humorístico característico de Alex."""

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