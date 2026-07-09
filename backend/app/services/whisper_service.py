from faster_whisper import WhisperModel

from app.config import (
    WHISPER_MODEL,
    DEVICE,
    COMPUTE_TYPE
)


class WhisperService:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            print("=" * 60)
            print("LOADING WHISPER MODEL...")
            print(f"Model        : {WHISPER_MODEL}")
            print(f"Device       : {DEVICE}")
            print(f"Compute Type : {COMPUTE_TYPE}")
            print("=" * 60)

            cls._model = WhisperModel(

                WHISPER_MODEL,

                device=DEVICE,

                compute_type=COMPUTE_TYPE

            )

            print("Whisper model loaded successfully.\n")

        return cls._model

    @staticmethod
    def transcribe(audio_path: str):

        model = WhisperService.get_model()

        segments, info = model.transcribe(

            audio_path,

            language="en",

            beam_size=5,

            best_of=5,

            temperature=0,

            vad_filter=True,

            word_timestamps=True

        )

        transcript = []

        words = []

        for segment in segments:

            transcript.append(segment.text.strip())

            if segment.words:

                for word in segment.words:

                    words.append(

                        {

                            "word": word.word.strip().lower(),

                            "start": round(word.start, 2),

                            "end": round(word.end, 2),

                            "confidence": round(word.probability, 3)

                        }

                    )

        return {

            "transcript": " ".join(transcript),

            "words": words,

            "language": info.language,

            "language_probability": round(
                info.language_probability,
                3
            )

        }