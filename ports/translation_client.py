from abc import ABC, abtractmethod

class TranslationClient(ABC):
    def translate(self, text: list[str]) -> list[str]:
        raise NotImplementedError