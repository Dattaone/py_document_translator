from abc import ABC, abstractmethod
from domain.entities.text_unit import TextUnit

class ExtractorPort(ABC):

    @abstractmethod
    def extract(self, path:str) -> list[TextUnit]:
        pass