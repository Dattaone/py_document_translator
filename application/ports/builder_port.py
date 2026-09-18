from abc import ABC, abstractmethod
from domain.entities.text_unit import TextUnit

class BuilderPort(ABC):

    @abstractmethod
    def build(self, translated_units:list[TextUnit], path:str):
        pass