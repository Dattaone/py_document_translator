from application.ports.translator_port import TranslatorPort
from domain.entities.chunk import Chunk

class FakeTranslator(TranslatorPort):
    def translate(self, chunks: list[Chunk], target_lang:str, source_lang:str = "en") ->list[str]:
        return [f"[{source_lang}->{target_lang}]{chunk.text}" for chunk in chunks]
    pass