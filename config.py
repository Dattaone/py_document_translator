import os
import sys
from dotenv import load_dotenv
from pathlib import Path

APP_NAME = "py_document_translator"

def _is_frozen()->bool:
    return getattr(sys, "frozen", False)

def _get_base_path()->Path:
    if _is_frozen():
        return Path.home() / APP_NAME
    else:
        return Path(__file__).resolve().parent
    

BASE_DIR = _get_base_path()

OUTPUT_DIR = BASE_DIR / "data"

TRANSLATIONS_DIR = OUTPUT_DIR / "translations"

def ensure_dirs():
    for path in(OUTPUT_DIR, TRANSLATIONS_DIR):
        path.mkdir(parents=True,exist_ok=True)

ensure_dirs()
load_dotenv()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")