from infrastructure.fake_translator import FakeTranslator
from domain.models import Chunk

def test_translator_returns_translated_text():
    translator = FakeTranslator()

    chunks= [
        Chunk(id=1, paragraph_ids=[1,2], text="Hello World"),
        Chunk(id=2, paragraph_ids=[3], text="Goodbye")
    ]

    result = translator.translate(chunks,target_lang="es")

    assert len(result) == 2
    assert result[0].startswith("[es]")
    assert "Hello World" in result[0]