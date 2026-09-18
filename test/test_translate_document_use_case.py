import os

from infrastructure.config.paths import OUTPUT_DIR

from infrastructure.documents.docx_extractor import DocxExtractor
from domain.services.chunker import Chunker
from infrastructure.translators.google_translator_requests import GoogleTranslatorRequests
from domain.services.mapper import Mapper
from infrastructure.documents.docx_builder import DocxBuilder 

from application.use_cases.translate_document_use_case import TranslateDocumentUseCase

from infrastructure.logging.logging_config import setup_logging

def test_translate_document_use_case():
    setup_logging()

    extractor = DocxExtractor()
    chunker = Chunker()
    translator = GoogleTranslatorRequests()
    mapper = Mapper()
    builder = DocxBuilder()
    use_case = TranslateDocumentUseCase(
        extractor   = extractor,
        chunker     = chunker,
        translator  = translator,
        mapper      = mapper,
        builder     = builder
    )
 
    file_name = "prueba.docx"
    use_case.execute(file_name)
    assert os.path.exists(f"data/translations/traducido_{file_name}")
    assert os.path.getsize(f"data/translations/traducido_{file_name}") > 0
    
