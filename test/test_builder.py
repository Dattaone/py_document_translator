import os

from infrastructure.documents.docx_builder import DocxBuilder
from infrastructure.documents.docx_extractor import DocxExtractor
from infrastructure.config.paths import OUTPUT_DIR

from domain.services.chunker import Chunker
from domain.entities.text_unit import TextUnit

def test_builder_by_text_units():
    builder = DocxBuilder()
    extractor = DocxExtractor()
    file_name = "te verde cap 2.docx"

    units = extractor.extract("prueba.docx")

    
    """ 
    units = [
        TextUnit(id=1, type="paragraph", text="Hello world"),
        TextUnit(id=2, type="paragraph", text="This is a test"),
        TextUnit(id=3, type="paragraph", text="Another paragraph")
    ] 
    """
   

    chunker = Chunker()
    chunk = chunker.chunk(units)

    is_create = builder.build(chunk, file_name)

    assert is_create == True
    assert os.path.exists(f"data/{file_name}")
    assert os.path.getsize(f"data/{file_name}") > 0
        
