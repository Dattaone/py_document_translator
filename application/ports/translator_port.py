from abc import ABC, abstractmethod
from domain.entities.chunk import Chunk

class TranslatorPort(ABC):

    @abstractmethod
    def translate(self, chunks: list[Chunk], target_lang:str, source_lang:str) -> list[Chunk]:
        pass