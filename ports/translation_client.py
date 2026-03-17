from abc import ABC, abstractmethod
from domain.models import Chunk

class TranslationClient(ABC):

    @abstractmethod
    def translate(self, chunks: list[Chunk], target_lang:str) -> list[str]:
        pass