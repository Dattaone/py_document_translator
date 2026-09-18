from infrastructure.config.settings import SEGMENT_SEPARATOR
from domain.entities.text_unit import TextUnit
from domain.entities.chunk import Chunk

class Chunker:

    def __init__(self, max_length=5000):
        self.max_length = max_length

    def chunk(self, units: list[TextUnit]) -> list[Chunk]:
        chunks = []
        unit_ids = []
        text = ""
        chunk_id = 0

        for i, unit in enumerate(units):
            candidate = unit.text + SEGMENT_SEPARATOR
            if i == len(units)-1:
                candidate = unit.text
                
            if len(text) + len(candidate) < self.max_length:
                text += candidate
                unit_ids.append(unit.id)
                continue
            
            chunks.append(Chunk(
                id              = chunk_id,
                unit_ids        = unit_ids.copy(),
                text            = text.removesuffix(SEGMENT_SEPARATOR)
            ))
            chunk_id += 1

            text = candidate
            unit_ids = [unit.id]
        
        if text:
            chunks.append(
                Chunk(
                    id          = chunk_id,
                    unit_ids    = unit_ids.copy(),
                    text        = text
                )
            )

        return chunks

        