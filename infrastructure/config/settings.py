import os
from dotenv import load_dotenv

load_dotenv()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
SEGMENT_SEPARATOR = os.getenv("SEGMENT_SEPARATOR")