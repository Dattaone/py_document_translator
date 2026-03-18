from infrastructure.google_translate_client import GoogleTranslator
from domain.models import Chunk

def test_google_translator_basic():
    translator = GoogleTranslator()

    chunks = [
        Chunk(id=1, paragraph_ids=[1], text="Hello world")
    ]

    result = translator.translate(chunks,target_lang="es")

    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], str)