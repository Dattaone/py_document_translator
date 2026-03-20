import requests
from config import DEEPL_API_KEY

from application.ports.translation_client import TranslationClient
from domain.models import Chunk

class GoogleTranslatorLib(TranslationClient):
    def __init__(self):
        self.url = "https://api-free.deepl.com/v2/translate"

    def _translate_text(self, text: str, target_lang: str)->str:
        data = {
            "text" : text,
            "target_lang": target_lang
        }
        headers = {
            "Authorization": f"DeepL-Auth-Key{DEEPL_API_KEY}"
        }
        response = requests.post(self.url, data=data, headers=headers)
        result = response.json()
        return result[0][0][0]
    
    def translate(self, chunks, target_lang):
        return [
            self._translate_text(chunk.text, target_lang) for chunk in chunks
        ]
