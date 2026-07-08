from pathlib import Path

from app.services.audio_service import AudioService
from app.services.whisper_service import WhisperService
from app.services.scoring_service import ScoringService
from app.services.feedback_service import FeedbackService


class PronunciationService:

    @staticmethod
    async def analyze(audio_file, reference_text: str):

        saved_file = await AudioService.save_audio(audio_file)

        wav_file = None

        try:

            # -----------------------------------------
            # Validate Audio Duration
            # -----------------------------------------

            duration = AudioService.get_duration(saved_file)

            AudioService.validate_duration(duration)

            # -----------------------------------------
            # Convert Audio to WAV
            # -----------------------------------------

            wav_file = AudioService.convert_to_wav(saved_file)

            # -----------------------------------------
            # Speech-to-Text (Faster Whisper)
            # -----------------------------------------

            whisper_result = WhisperService.transcribe(wav_file)

            transcript = whisper_result["transcript"]

            word_details = whisper_result["words"]

            # -----------------------------------------
            # Pronunciation Analysis
            # -----------------------------------------

            score_result = ScoringService.calculate_word_score(

                reference_text=reference_text,

                transcript=transcript,

                whisper_words=word_details

            )

            # -----------------------------------------
            # User Feedback
            # -----------------------------------------

            feedback = FeedbackService.generate_feedback(

                score_result["analysis"]

            )

            # -----------------------------------------
            # API Response
            # -----------------------------------------

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

                # Only words requiring attention
                "analysis": score_result["analysis"],

                "feedback": feedback

            }

        finally:

            try:

                if saved_file and Path(saved_file).exists():

                    AudioService.delete_file(saved_file)

            except Exception:

                pass

            try:

                if wav_file and Path(wav_file).exists():

                    AudioService.delete_file(wav_file)

            except Exception:

                pass