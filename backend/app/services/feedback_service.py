from typing import List, Dict


class FeedbackService:

    @staticmethod
    def generate_feedback(analysis: List[Dict]) -> List[Dict]:

        mispronounced = []
        unclear = []
        missing = []
        extra = []

        for item in analysis:

            status = item.get("status")

            if status == "mispronounced":
                mispronounced.append(item.get("expected"))

            elif status == "unclear":
                unclear.append(item.get("expected"))

            elif status == "missing":
                missing.append(item.get("expected"))

            elif status == "extra":
                extra.append(item.get("spoken"))

        feedback = []

        if mispronounced:

            feedback.append(
                {
                    "title": "Mispronounced Words",
                    "words": mispronounced,
                    "message": (
                        "These words were recognized differently from the reference. "
                        "Try pronouncing them more clearly."
                    )
                }
            )

        if unclear:

            feedback.append(
                {
                    "title": "Unclear Pronunciation",
                    "words": unclear,
                    "message": (
                        "These words were recognized but were not pronounced clearly. "
                        "Speak a little slower and emphasize each syllable."
                    )
                }
            )

        if missing:

            feedback.append(
                {
                    "title": "Missing Words",
                    "words": missing,
                    "message": (
                        "These words were not detected in your speech. "
                        "Try speaking the complete sentence."
                    )
                }
            )

        if extra:

            feedback.append(
                {
                    "title": "Extra Words",
                    "words": extra,
                    "message": (
                        "These words do not appear in the reference sentence."
                    )
                }
            )

        if not feedback:

            feedback.append(
                {
                    "title": "Excellent!",
                    "words": [],
                    "message": (
                        "Excellent pronunciation! No significant pronunciation issues were detected."
                    )
                }
            )

        return feedback