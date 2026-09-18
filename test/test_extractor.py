from infrastructure.documents.docx_extractor import DocxExtractor
from infrastructure.config.paths import OUTPUT_DIR

def test_extractor_returns_text_units():
    extractor = DocxExtractor()
    test_docx = "prueba.docx"
    units = extractor.extract(test_docx)
    
    assert units is not None
    assert len(units) > 0
    assert units[0].text != ""

