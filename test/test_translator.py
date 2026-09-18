from infrastructure.translators.fake_translator import FakeTranslator
from domain.entities.chunk import Chunk

def test_translator_returns_translated_text():
    translator = FakeTranslator()

    chunks= [
        Chunk(id=1, unit_ids=[1,2], text="Hello World"),
        Chunk(id=2, unit_ids=[3], text="Goodbye")
    ]

    result = translator.translate(chunks,target_lang="es")

    assert len(result) == 2
    assert result[0].startswith("[es]")
    assert "Hello World" in result[0]