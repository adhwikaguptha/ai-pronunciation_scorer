from pathlib import Path
from uuid import uuid4
import time

from fastapi import UploadFile, HTTPException
from pydub import AudioSegment

from app.config import (
    UPLOAD_DIR,
    MIN_AUDIO_DURATION,
    MAX_AUDIO_DURATION,
)


ALLOWED_EXTENSIONS = {
    ".wav",
    ".mp3",
    ".m4a",
    ".ogg",
    ".oga",
    ".opus",
    ".flac",
    ".webm"
}


class AudioService:

    @staticmethod
    async def save_audio(file: UploadFile) -> Path:
        """
        Save uploaded audio to disk.
        """

        extension = Path(file.filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Unsupported audio format."
            )

        filename = f"{uuid4()}{extension}"

        file_path = UPLOAD_DIR / filename

        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        return file_path

    @staticmethod
    def get_duration(file_path: Path) -> float:
        """
        Returns duration in seconds.
        """

        start = time.time()

        audio = AudioSegment.from_file(file_path)

        print(
            f"get_duration -> AudioSegment.from_file: "
            f"{time.time() - start:.2f} sec"
        )

        duration = len(audio) / 1000

        return duration

    @staticmethod
    def validate_duration(duration: float):

        if duration < MIN_AUDIO_DURATION:

            raise HTTPException(
                status_code=400,
                detail=f"Audio must be at least {MIN_AUDIO_DURATION} seconds."
            )

        if duration > MAX_AUDIO_DURATION:

            raise HTTPException(
                status_code=400,
                detail=f"Audio must not exceed {MAX_AUDIO_DURATION} seconds."
            )

    @staticmethod
    def convert_to_wav(file_path: Path) -> Path:
        """
        Converts uploaded audio into WAV format.

        Whisper performs best with WAV.
        """

        start = time.time()

        audio = AudioSegment.from_file(file_path)

        print(
            f"convert_to_wav -> AudioSegment.from_file: "
            f"{time.time() - start:.2f} sec"
        )

        wav_path = file_path.with_suffix(".wav")

        start = time.time()

        audio.export(
            wav_path,
            format="wav"
        )

        print(
            f"convert_to_wav -> Export WAV: "
            f"{time.time() - start:.2f} sec"
        )

        return wav_path

    @staticmethod
    def delete_file(file_path: Path):

        if file_path.exists():

            file_path.unlink()