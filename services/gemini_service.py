"""
==========================================================
EduAssess AI
----------------------------------------------------------
Module      : Gemini Service
Author      : Dr. Jagdish Raj Saini & ChatGPT
Version     : 0.7.0
Description : Handles communication with Google Gemini
==========================================================
"""

from google import genai
from google.genai import types

from config import GEMINI_API_KEYS
from config import MODEL

from models.assessment_output import AssessmentOutput


class GeminiService:
    """
    Handles communication with Google Gemini.

    Features
    --------
    ✓ Multiple API Keys
    ✓ Persistent Round-Robin
    ✓ Automatic Failover
    ✓ Friendly Error Messages
    """

    _last_successful_index = -1

    def __init__(self):
        pass

    def generate(self, prompt: str) -> str:
        """
        Generate assessment using Gemini.

        Starts from the API key after the last successful key.
        Automatically switches keys when quota is exhausted.
        """

        total_keys = len(GEMINI_API_KEYS)

        if total_keys == 0:

            raise RuntimeError("No Gemini API Keys configured.")

        start_index = (GeminiService._last_successful_index + 1) % total_keys

        last_error = None

        for attempt in range(total_keys):

            current_index = (start_index + attempt) % total_keys

            api_key = GEMINI_API_KEYS[current_index]

            try:

                print(f"[Gemini] Using API Key {current_index + 1}")
                print(f"({MODEL})")

                client = genai.Client(api_key=api_key)

                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.3,
                        response_mime_type="application/json",
                        response_schema=AssessmentOutput,
                    ),
                )

                # -------------------------------------------------------------
                # Remember successful key
                # -------------------------------------------------------------

                GeminiService._last_successful_index = current_index

                print(
                    f"[Gemini] Successfully generated assessment "
                    f"using API Key {current_index + 1}"
                )

                return response.text

            except Exception as error:

                message = str(error)

                # ---------------------------------------------------------
                # Quota exhausted or Auth Error -> Try next key
                # ---------------------------------------------------------

                if (
                    "429" in message
                    or "RESOURCE_EXHAUSTED" in message
                    or "503" in message
                    or "UNAVAILABLE" in message
                    or "401" in message  # <-- NEW: Catch bad keys
                    or "UNAUTHENTICATED" in message  # <-- NEW: Catch bad keys
                ):

                    print(
                        f"[Gemini] API Key {current_index + 1} "
                        "temporarily unavailable or invalid. Trying next key..."
                    )

                    last_error = error

                    continue

                # ---------------------------------------------------------
                # Any other Gemini error
                # ---------------------------------------------------------

                raise RuntimeError(f"Gemini Error:\n\n{message}")

        raise RuntimeError(
            "🚫 AI Service Temporarily Unavailable\n\n"
            "All configured Gemini API Keys have reached "
            "their usage limits.\n\n"
            "Please wait for the quota to reset "
            "or add another API Key.\n\n"
            "Your previously generated assessments "
            "remain available for review."
        ) from last_error
