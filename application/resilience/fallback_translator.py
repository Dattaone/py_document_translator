from application.ports.translation_client import TranslationClient
from application.resilience.retry_translator import  RetryTranslator
class FallbackTranslator(TranslationClient):
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    def translate(self, chunks, target_lang):
        try:
            return RetryTranslator(self.primary.translate(chunks,target_lang))
        except Exception:
            print("fallback activado")
            return self.secondary.translate(chunks,target_lang)