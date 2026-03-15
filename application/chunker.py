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
       pass