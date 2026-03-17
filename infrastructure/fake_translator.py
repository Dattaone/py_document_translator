from ports.translation_client import TranslationClient
from domain.models import Chunk

class FakeTranslator(TranslationClient):
    def translate(self, chunks: list[Chunk], target_lang:str) ->list[str]:
        return [f"[{target_lang}]{chunk.text}" for chunk in chunks]
    pass