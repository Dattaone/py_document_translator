from infrastructure.logging.logging_config import setup_logging


from infrastructure.documents.docx_extractor import DocxExtractor
from domain.services.chunker import Chunker
from infrastructure.translators.google_translator_requests import GoogleTranslatorRequests
from domain.services.mapper import Mapper
from infrastructure.documents.docx_builder import DocxBuilder 

from application.use_cases.translate_document_use_case import TranslateDocumentUseCase



def main():
    setup_logging()
    
    """ 
    
    extractor = DocxExtractor()
    chunker = Chunker()
    mapper = Mapper()    
    builder = DocxBuilder()

    file_name = "prueba.docx"

    units = extractor.extract(file_name)
    chunks = chunker.chunk(units)


    import logging
    logger = logging.getLogger(__name__)

    units_ids = []
    text = ""
    for i, chunk in enumerate(chunks):
        print(f"chunk {i}: {chunk}\n\n")
        logger.info(f"{chunk.text}\n")
        units_ids.append([id for id in chunk.unit_ids])
        text += chunk.text

    count = text.count("⟪SEP⟫")

    split = text.split("⟪SEP⟫")


    logger.info(f"ids: {units_ids}")
    logger.info(f"count: {count}")
    logger.info(f"count_split: {len(split)}")
    """
    



     
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
    

if __name__ == "__main__":
    main()