from application.ports.extractor_port import ExtractorPort
from application.ports.translator_port import TranslatorPort
from application.ports.builder_port import BuilderPort

import logging
logger = logging.getLogger(__name__)

class TranslateDocumentUseCase:

    def __init__(
        self,
        extractor: ExtractorPort,
        chunker,
        translator: TranslatorPort,
        mapper,
        builder: BuilderPort
    ):
        self.extractor  = extractor
        self.chunker    = chunker
        self.translator = translator
        self.mapper     = mapper
        self.builder    = builder

    def execute(self, path):
        logger.info(f"Iniciando traduccion: {path}")

        units = self.extractor.extract(path)
        logger.info(f"Documento extraído: {len(units)} unidades")

        chunks = self.chunker.chunk(units)
        logger.info(f"Documento dividido en {len(chunks)} chunks")

        
        translated_chunks = self.translator.translate(chunks=chunks, source_lang="es", target_lang="en")
        logger.info(f"Chunks traducidos: {len(translated_chunks)}")
        

        translated_units = self.mapper.mapp(
            units,
            translated_chunks
        )
        logger.info(f"Unidades reconstruidas: {len(translated_units)}")
        

        self.builder.build(
            translated_units,
            path
        )
        logger.info(f"Traducción finalizada")