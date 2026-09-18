import os
from docx import Document
from application.ports.extractor_port import ExtractorPort
from infrastructure.config.paths import OUTPUT_DIR
from domain.entities.text_unit import TextUnit, TextUnitType

class DocxExtractor(ExtractorPort):
    def extract(self, path:str) -> list[TextUnit]:
        file_path = os.path.join(OUTPUT_DIR, path)
        doc = Document(file_path)
        units = []

        for index, p in enumerate(doc.paragraphs):
            style = p.style.name
            if p.style.name.startswith("Heading"):
                #level = int(p.style.name[-1])
                units.append(TextUnit(
                        id          = index, 
                        type        = TextUnitType.HEADING, 
                        text        = p.text, 
                        metadata    = {
                                "style": style,
                                "runs" : [
                                    {
                                        "text"      : run.text,
                                        "bold"      : run.bold,
                                        "italic"    : run.italic,
                                        "underline" : run.underline,
                                    }
                                    for run in p.runs
                                ]
                            }
                        ))
            else:
                units.append(TextUnit(
                    id          = index, 
                    type        = TextUnitType.PARAGRAPH, 
                    text        = p.text,
                    metadata    = {
                            "style": style,
                            "runs" : [
                                {
                                    "text"      : run.text,
                                    "bold"      : run.bold,
                                    "italic"    : run.italic,
                                    "underline" : run.underline,
                                }
                                for run in p.runs
                            ]
                        }
                    ))

        return units
