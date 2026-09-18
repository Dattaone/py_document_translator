import requests
from application.ports.translator_port import TranslatorPort
from domain.entities.chunk import Chunk

import logging
logger = logging.getLogger(__name__)

class GoogleTranslatorRequests(TranslatorPort):


    def _translate_text(self, text: str, source_lang:str = "en", target_lang:str = "es") -> str:
        params = {
            "client": "gtx",
            "sl": source_lang, #IDIOMA DE ORIGEN
            "tl": target_lang, #IDIOMA DE DESTINO
            "dt": "t",
            "q": text
        }

        try:
            response = requests.get("https://translate.googleapis.com/translate_a/single", params=params, timeout=10)
            response.raise_for_status()
            result = response.json()

            if result and isinstance(result, list):
                return result[0][0][0]

            return text

        except Exception as e:
            logger.warning(f"⚠️ Error en GoogleTranslation {e}")
            raise 

    def translate(self, chunks: list[Chunk], target_lang: str, source_lang:str) -> list[Chunk]:
        translated_chunks = []
        for chunk in chunks:
            chunk.text = self._translate_text(chunk.text, target_lang=target_lang, source_lang=source_lang)
            translated_chunks.append(
                chunk
            )
        return translated_chunks