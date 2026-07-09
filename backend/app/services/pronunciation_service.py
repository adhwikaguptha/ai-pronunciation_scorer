from pathlib import Path
import time

from app.services.audio_service import AudioService
from app.services.whisper_service import WhisperService
from app.services.scoring_service import ScoringService
from app.services.feedback_service import FeedbackService


class PronunciationService:

    @staticmethod
    async def analyze(audio_file, reference_text: str):

        total_start = time.time()

        print("=" * 60)
        print("New Pronunciation Analysis Request")

        saved_file = await AudioService.save_audio(audio_file)

        wav_file = None

        try:

            # -----------------------------------------
            # Duration Validation
            # -----------------------------------------

            start = time.time()

            duration = AudioService.get_duration(saved_file)

            AudioService.validate_duration(duration)

            print(f"Duration Validation : {time.time() - start:.2f} sec")

            # -----------------------------------------
            # Audio Conversion
            # -----------------------------------------

            start = time.time()

            wav_file = AudioService.convert_to_wav(saved_file)

            print(f"WAV Conversion      : {time.time() - start:.2f} sec")

            # -----------------------------------------
            # Whisper
            # -----------------------------------------

            start = time.time()

            whisper_result = WhisperService.transcribe(wav_file)

            print(f"Whisper Inference   : {time.time() - start:.2f} sec")

            transcript = whisper_result["transcript"]

            word_details = whisper_result["words"]

            # -----------------------------------------
            # Scoring
            # -----------------------------------------

            start = time.time()

            score_result = ScoringService.calculate_word_score(

                reference_text=reference_text,

                transcript=transcript,

                whisper_words=word_details

            )

            print(f"Scoring             : {time.time() - start:.2f} sec")

            # -----------------------------------------
            # Feedback
            # -----------------------------------------

            start = time.time()

            feedback = FeedbackService.generate_feedback(

                score_result["analysis"]

            )

            print(f"Feedback            : {time.time() - start:.2f} sec")

            print("-" * 60)
            print(f"TOTAL REQUEST TIME  : {time.time() - total_start:.2f} sec")
            print("=" * 60)

            return {

                "success": True,

                "score": score_result["score"],

                "accuracy": score_result["accuracy"],

                "reference_text": reference_text,

                "transcript": transcript,

                "language": whisper_result["language"],

                "language_probability": round(
                    whisper_result["language_probability"],
                    3
                ),

                "duration": round(duration, 2),

                "analysis": score_result["analysis"],

                "feedback": feedback

            }

        finally:

            try:

                if saved_file and Path(saved_file).exists():

                    AudioService.delete_file(saved_file)

            except Exception as e:

                print(f"Cleanup Error (audio): {e}")

            try:

                if wav_file and Path(wav_file).exists():

                    AudioService.delete_file(wav_file)

            except Exception as e:

                print(f"Cleanup Error (wav): {e}")