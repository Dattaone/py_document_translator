""" 
Convertir lista de párrafos -> lista de chunks (No sabe nada de JSON)
Aquí metes tu lógica de:
• Máximo caracteres
• No cortar párrafos
• Mantener contexto
"""
from domain.models import ParagraphUnit, Chunk
class Chunker:

    def __init__(self, max_length=5000):
        self.max_length = max_length

    def chunk(self, units: list[ParagraphUnit]) -> list[Chunk]:
        chunks = []
        paragraph_ids = []
        text = ""
        chunk_id = 0

        for unit in units:
            candidate = unit.text + "<SEP>"
            if len(text) + len(candidate) <= self.max_length:
                text += candidate
                paragraph_ids.append(unit.id)
                continue
            
            chunks.append(Chunk(
                id              = chunk_id,
                paragraph_ids   = paragraph_ids.copy(),
                text            = text
            ))
            chunk_id += 1

            text = candidate
            paragraph_ids = [unit.id]
        
        if text:
            chunks.append(
                Chunk(
                    id=chunk_id,
                    paragraph_ids= paragraph_ids.copy(),
                    text = text
                )
            )

        return chunks

        