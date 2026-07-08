import re
from difflib import SequenceMatcher

from rapidfuzz import fuzz


class ScoringService:

    @staticmethod
    def normalize(text: str):

        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @staticmethod
    def calculate_word_score(

        reference_text: str,

        transcript: str,

        whisper_words: list

    ):

        reference = ScoringService.normalize(reference_text)
        spoken = ScoringService.normalize(transcript)

        reference_words = reference.split()
        spoken_words = spoken.split()

        matcher = SequenceMatcher(

            None,

            reference_words,

            spoken_words

        )

        analysis = []

        similarity_sum = 0
        matched = 0
        missing = 0

        whisper_index = 0

        for tag, i1, i2, j1, j2 in matcher.get_opcodes():

            # ---------------------------------
            # Correctly aligned words
            # ---------------------------------

            if tag == "equal":

                for ref, spk in zip(

                    reference_words[i1:i2],

                    spoken_words[j1:j2]

                ):

                    similarity = fuzz.ratio(ref, spk)

                    confidence = 1.0

                    if whisper_index < len(whisper_words):

                        confidence = whisper_words[
                            whisper_index
                        ]["confidence"]

                    similarity_sum += similarity
                    matched += 1

                    # Confidence is used internally only
                    if confidence >= 0.90:

                        status = "correct"

                    elif confidence >= 0.70:

                        status = "unclear"

                    else:

                        status = "mispronounced"

                    # Only return words needing attention
                    if status != "correct":

                        analysis.append(

                            {

                                "expected": ref,

                                "spoken": spk,

                                "similarity": round(similarity, 2),

                                "status": status

                            }

                        )

                    whisper_index += 1

            # ---------------------------------
            # Replaced words
            # ---------------------------------

            elif tag == "replace":

                ref_chunk = reference_words[i1:i2]

                spk_chunk = spoken_words[j1:j2]

                max_len = max(

                    len(ref_chunk),

                    len(spk_chunk)

                )

                for k in range(max_len):

                    expected = (

                        ref_chunk[k]

                        if k < len(ref_chunk)

                        else ""

                    )

                    actual = (

                        spk_chunk[k]

                        if k < len(spk_chunk)

                        else ""

                    )

                    similarity = fuzz.ratio(

                        expected,

                        actual

                    )

                    similarity_sum += similarity
                    matched += 1

                    analysis.append(

                        {

                            "expected": expected,

                            "spoken": actual,

                            "similarity": round(similarity, 2),

                            "status": "mispronounced"

                        }

                    )

                    whisper_index += 1

            # ---------------------------------
            # Missing words
            # ---------------------------------

            elif tag == "delete":

                for word in reference_words[i1:i2]:

                    missing += 1

                    analysis.append(

                        {

                            "expected": word,

                            "spoken": "",

                            "status": "missing"

                        }

                    )

            # ---------------------------------
            # Extra words
            # ---------------------------------

            elif tag == "insert":

                for word in spoken_words[j1:j2]:

                    analysis.append(

                        {

                            "expected": "",

                            "spoken": word,

                            "status": "extra"

                        }

                    )

        # ---------------------------------
        # Metrics
        # ---------------------------------

        accuracy = (

            similarity_sum / matched

            if matched

            else 0

        )

        completeness = (

            ((len(reference_words) - missing)

             / len(reference_words)) * 100

            if reference_words

            else 0

        )

        # Final pronunciation score
        final_score = (

            accuracy * 0.70 +

            completeness * 0.30

        )

        final_score = max(

            0,

            min(

                100,

                final_score

            )

        )

        return {

            "score": round(final_score, 2),

            "accuracy": round(accuracy, 2),

            "analysis": analysis

        }