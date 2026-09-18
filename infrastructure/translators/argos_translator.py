import requests
from application.ports.translator_port import TranslatorPort
from domain.entities.chunk import Chunk

import argostranslate.package
import argostranslate.translate

import logging
logger = logging.getLogger(__name__)

class ArgosTranslatorRequests(TranslatorPort):

    def _translate_text(self, source_text:str, target_lang:str = "es", source_lang:str = "en"):

        translated_text = argostranslate.translate.translate(
            q           = source_text, 
            from_code   = source_lang, 
            to_code     = target_lang
        )
        
        return translated_text

    def translate(self, chunks:list[Chunk], target_lang:str, source_lang:str):
        translated_chunks = []
        for chunk in chunks:
            chunk.text = self._translate_text(chunk.text, target_lang=target_lang, source_lang=source_lang)
            translated_chunks.append(
                chunk
            )
        return translated_chunks
