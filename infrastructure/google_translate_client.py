import requests
from ports.translation_client import TranslationClient
from domain.models import Chunk


class GoogleTranslator(TranslationClient):

    def _init_(self):
        self.url_translator = "https://translate.googleapis.com/translate_a/single"

    def _translate_text(self, text: str, target_lang: str) -> str:
        params = {
            "client": "gtx",
            "sl": "en",
            "tl": target_lang,
            "dt": "t",
            "q": text
        }

        try:
            response = requests.get(self.url_translator, params=params, timeout=10)
            response.raise_for_status()
            result = response.json()

            if result and isinstance(result, list):
                return result[0][0][0]

            return text

        except Exception as e:
            print(f"⚠️ Error en traducción: {e}")
            return text

    def translate(self, chunks: list[Chunk], target_lang: str) -> list[str]:
        return [
            self._translate_text(chunk.text, target_lang) for chunk in chunks
        ]