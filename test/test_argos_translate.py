from infrastructure.translators.argos_translator import ArgosTranslatorRequests
from domain.entities.chunk import Chunk

def test_argos_translator_requests():
    translator = ArgosTranslatorRequests()

    source_lang = "en"
    target_lang = "es"
    example_text = "why she had to go. i don't know. she wouldn't say. I said something wrong, now i long for yesterday."

    chunks = [
        Chunk(id=1, unit_ids=[1], text=example_text)
    ]

    result = translator.translate(
        chunks      =chunks, 
        target_lang =target_lang, 
        source_lang =source_lang
    )

    print(f"{result[0].text}")
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0].text, str)