from ports.translation_client import TranslationClient
class FallbackTranslator(TranslationClient):
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    def translate(self, chunks, target_lang):
        try:
            return self.primary.translate(chunks,target_lang)
        except Exception:
            print("fallback activado")
            self.secondary.translate(chunks,target_lang)