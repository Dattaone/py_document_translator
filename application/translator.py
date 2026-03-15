from domain.models import ParagraphUnit

class Translator:
    def __init__(self, client):
        self.client = client
    
    def translate_chunks(self, chunks:list[ParagraphUnit])-> None:
        texts = [c.text for c in chunks]
        translated = self.client.translate(texts)
        