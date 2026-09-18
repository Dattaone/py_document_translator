from infrastructure.config.settings import SEGMENT_SEPARATOR
from domain.entities.text_unit import TextUnit
from domain.entities.chunk import Chunk

import logging
logger = logging.getLogger(__name__)

class Mapper:

    def mapp(self, units:list[TextUnit], translated_chunks:list[Chunk])->list[TextUnit]:


        translated_mapped = []
        for chunk in translated_chunks:
            translated_texts = chunk.text.split(SEGMENT_SEPARATOR)

            translated_texts = chunk.text.split(SEGMENT_SEPARATOR)

            logger.info("UNIT IDS:", len(chunk.unit_ids))
            logger.info("TEXTS:", len(translated_texts))
            logger.info("LAST TEXT:", repr(translated_texts[-1]))
            logger.info("ENDS WITH SEP:", chunk.text.endswith(SEGMENT_SEPARATOR))

            if len(chunk.unit_ids) != len(translated_texts):
                logger.error(
                    "Chunk %d inconsistentes: %d IDs, %d textos",
                    chunk.id,
                    len(chunk.unit_ids),
                    len(translated_texts)
                )


            for index, translated_text in enumerate(translated_texts):
                
                text_unit_id = chunk.unit_ids[index]
                raw_text = next((unit for unit in units if unit.id == text_unit_id))
                translated_mapped.append(
                    TextUnit(
                        id          = raw_text.id,
                        type        = raw_text.type,
                        text        = translated_text,
                        metadata    = raw_text.metadata
                    )
                )
        
        return translated_mapped
            
        #PASOS A SEGUIR
        #juntar todo el texto
        #recorrer todo el texto 
        #for de los units
        #buscar cada sep en especifico segun unit id
        #reemplazar el text del unit por el traducido
        #mandar el units editado
