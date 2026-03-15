""" 
Extructura pura de datos.(Nada de lógica, solo representan datos)
• ParagraphUnit
• Chunk
• TranslationUnit
"""

from dataclasses import dataclass

@dataclass
class ParagraphUnit:
    id      : int
    type    : str   # "paragraph" or "chunk"
    text    : str
    level   : int | None = None #solo si es heading

