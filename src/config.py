from dotenv import load_dotenv, dotenv_values

class Config:
    def __init__(self):
        load_dotenv()
        for key, value in dotenv_values().items():
            setattr(self, key, value)

    def get(self, key, default=None) -> str:
        return getattr(self, key, default)