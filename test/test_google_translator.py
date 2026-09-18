from infrastructure.translators.google_translator_requests import GoogleTranslatorRequests
from infrastructure.translators.google_translator_lib import GoogleTranslatorLib
from domain.entities.chunk import Chunk

def test_google_translator_basic():
    translator = GoogleTranslatorRequests()

    target_lang = "es"
    source_lang = "en"
    example_text = "why she had to go. i don't know. she wouldn't say. I said something wrong. Now i long for yesterday."

    chunks = [
        Chunk(id=1, unit_ids=[1], text=example_text)
    ]

    result = translator.translate(chunks,target_lang=target_lang, source_lang=source_lang)

    print(f"{result[0].text}")
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0].text, str)