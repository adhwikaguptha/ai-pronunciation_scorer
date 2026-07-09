from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


MIN_AUDIO_DURATION = 30
MAX_AUDIO_DURATION = 300


WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")


DEVICE = os.getenv("DEVICE", "cpu")

COMPUTE_TYPE = os.getenv("COMPUTE_TYPE", "int8")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"