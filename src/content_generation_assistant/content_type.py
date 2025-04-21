from abc import ABC, abstractmethod

class ContentType(ABC):
    # def __init__(self):
    #     super().__init__()

    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_example(self) -> str:
        pass

    @abstractmethod
    def get_preferred_temperature(self) -> int:
        pass

    @abstractmethod
    def get_context(self) -> str:
        pass