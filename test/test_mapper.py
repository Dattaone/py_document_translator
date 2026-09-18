from infrastructure.documents.docx_extractor import DocxExtractor
from infrastructure.config.paths import OUTPUT_DIR

from domain.services.chunker import Chunker
from domain.entities.text_unit import TextUnit

from domain.entities.chunk import Chunk
from infrastructure.translators.google_translator_requests import GoogleTranslatorRequests

from domain.services.mapper import Mapper

def test_mapper_create_mapp():
    extractor = DocxExtractor()
    test_docx = "te verde.docx"
    units = extractor.extract(OUTPUT_DIR/test_docx)
    assert units is not None
    assert units[0].text != ""


    chunker = Chunker()
    chunks = chunker.chunk(units)
    assert len(chunks) > 1


    translator = GoogleTranslatorRequests()
    translated_chunks = translator.translate(chunks, target_lang="en", source_lang="es")
    assert isinstance(translated_chunks, list)
    assert isinstance(translated_chunks[0].text, str)
    
    


    mapper = Mapper()
    translated_units = mapper.mapp(units, translated_chunks)
    for translated_unit in translated_units:
        print(f"\n\nid: {translated_unit.id}")
        print(f"text: {translated_unit.text}\n")
    assert translated_units is not None
    assert len(translated_units) > 0
    assert translated_units[2].text != ""
