import time
from application.ports import TranslationClient

class RetryTranslator(TranslationClient):
    def __init__(self, translator:TranslationClient, retries=3):
        self.translator = translator
        self.retries = retries

    def translate(self, text: str, target_lang: str)->str:
        delay = 1

        for attempt in range(self.retries):
            try:
                return self.translator.translate(text, target_lang)
            except Exception:
                if attempt == self.retries - 1:
                    raise time.sleep(delay)

    