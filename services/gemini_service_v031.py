"""
==========================================================
EduAssess AI
----------------------------------------------------------
Module      : Gemini Service
Author      : Dr. Jagdish Raj Saini & ChatGPT
Version     : 0.3.1
Description : Handles communication with Google Gemini
==========================================================
"""

from google import genai

from config import GEMINI_API_KEY
from config import MODEL


class GeminiService:
    """
    Handles all communication with Google Gemini.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to Gemini and returns the response.
        """

        try:

            response = self.client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            print("=" * 80)
            print(response.text)
            print("=" * 80)

            return response.text

        except Exception as error:

            raise RuntimeError(f"Gemini Error: {error}")