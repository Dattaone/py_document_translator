""" 
• Toma el docx original + JSON traducido
• Reemplaza texto respetando estructura
"""
import logging
from docx import Document
from domain.models import ParagraphUnit
class DocxBuilder:

    def build(
            self, 
            units: list[ParagraphUnit], 
            translations: list[str],
            output_path: str):
        try:
            pass
        except Exception as e:
            pass