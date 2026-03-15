""" 
Convertir DOCX -> lista oredenada de ParagraphUnit
No traduce. No chuncking. No lógica extra.
Solo extracción limpia
"""
from docx import Document
from domain.models import ParagraphUnit

class DocxExtractor:
    def extract(self, path:str) -> list[ParagraphUnit]:
        
        doc = Document(path)
        units = []

        for index, p in enumerate(doc.paragraphs):
            if p.style.name.startswith("Heading"):
                level = int(p.style.name[-1])
                units.append(ParagraphUnit(
                        id     = index, 
                        type   = "heading", 
                        text   = p.text, 
                        level  = level
                        ))
            else:
                units.append(ParagraphUnit(
                    id    = index, 
                    type  = "paragraph", 
                    text  = p.text
                    ))

        return units
