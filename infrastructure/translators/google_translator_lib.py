import requests
from infrastructure.config.settings import DEEPL_API_KEY
from application.ports.translator_port import TranslatorPort
from domain.entities.chunk import Chunk

class GoogleTranslatorLib(TranslatorPort):
    def __init__(self):
        self.url = "https://api-free.deepl.com/v2/translate"

    def _translate_text(self, text: str, target_lang: str, source_lang:str="en")->str:
        data = {
            "text" : text,
            "target_lang": target_lang,
            "source_lang": source_lang
        }
        headers = {
            "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"
        }
        response = requests.post(self.url, data=data, headers=headers)
        result = response.json()
        return result["translations"][0]["text"]
    
    def translate(self, chunks, target_lang, source_lang):
        return [
            self._translate_text(chunk.text, target_lang, source_lang) for chunk in chunks
        ]
