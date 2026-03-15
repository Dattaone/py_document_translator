import requests
from ports.translation_client import TranslationClient

class GoogleTranslateClient(TranslationClient):
    def translate(self, text: list[str])-> list[str]:
        pass 