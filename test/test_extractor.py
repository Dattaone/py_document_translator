from infrastructure.docx_extractor import DocxExtractor
from config import OUTPUT_DIR

def test_extractor_returns_paragraph_units():
    extractor = DocxExtractor()
    test_docx = "te verde.docx"
    units = extractor.extract(OUTPUT_DIR/test_docx)
    
    assert units is not None
    assert len(units) > 0
    assert units[0].text != ""

