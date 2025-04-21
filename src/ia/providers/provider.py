from abc import ABC, abstractmethod
from src.config import Config
from openai import OpenAI

class Provider(ABC):
    def __init__(self):
        self._temperature: float = 1.0
        self._max_tokens: int = 4092

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        if not (self.get_min_temperature() <= value <= self.get_max_temperature()):
            raise ValueError(f"Temperature must be an integer between {self.get_min_temperature()} and {self.get_max_temperature()} inclusive.")
        self._temperature = value

    @property
    def max_tokens(self) -> int:
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, value: int):
        if value <= 0 or value > 8192:
            raise ValueError("max_tokens must be a positive integer but depends on the model used.")
        self._max_tokens = value

    @abstractmethod
    def get_provider_name(self):
        pass

    @abstractmethod
    def get_min_temperature(self) -> float:
        pass

    @abstractmethod
    def get_max_temperature(self) -> float:
        pass

    @abstractmethod
    def get_client(self) -> OpenAI:
        pass

    @abstractmethod
    def make_request(self, client: OpenAI, context: str, question: str) -> object:
        pass

    @abstractmethod
    def get_response_text(self, response: object) -> str:
        pass

    def query(self, context: str, question: str) -> str:
        client = self.get_client()

        if not client:
            raise ValueError("ERROR: Client is not configured properly.")

        response = self.make_request(client, context, question)

        if not response:
            raise ValueError("ERROR: No response from the provider.")

        return self.get_response_text(response)

    def get_config(self, key:str) -> str:
        return Config().get(f"{self.get_provider_name().upper()}_{key.upper()}")
