"""
==========================================================
EduAssess AI
----------------------------------------------------------
Module      : Response Parser
Author      : Dr. Jagdish Raj Saini & ChatGPT
Version     : 3.1.1
Description : Parses and validates Gemini responses.
==========================================================
"""

import json
import re

from models.assessment_output import AssessmentOutput


class ResponseParser:
    """
    Parses Gemini responses into validated AssessmentOutput objects.
    """

    @staticmethod
    def _clean_invalid_escapes(text: str) -> str:
        """
        Fixes unescaped backslashes that cause JSON parsing errors.
        """
        return re.sub(r"\\u(?![0-9a-fA-F]{4})", r"\\\\u", text)

    @staticmethod
    def parse(response_text: str) -> AssessmentOutput:
        """
        Parse the JSON response returned by Gemini and validate it.
        """
        if not response_text:
            raise ValueError("Gemini returned an empty response.")

        def is_truncation(err: json.JSONDecodeError, text: str) -> bool:
            if len(text) < 40000:
                return False
            err_msg = str(err)
            if "Unterminated string" in err_msg or "Expecting" in err_msg:
                return True
            if "\\u" in err_msg and err.pos > len(text) - 20:
                return True
            return False

        try:
            # Attempt 1: Standard Parse
            data = json.loads(response_text)

        except json.JSONDecodeError as error:
            # Check 1: Did we hit the API token limit? (Massive text chunk)
            if is_truncation(error, response_text):
                raise ValueError(
                    "🛑 **Assessment Generation Incomplete**\n\n"
                    "The AI reached its maximum output limit before finishing all the questions. "
                    "Your detailed explanations are generating too much text for a single batch.\n\n"
                    "💡 **Fix:** Please reduce the 'Total Questions' (try 5 to 10 at a time) and generate again."
                ) from error

            # Check 2: Try cleaning invalid math escapes
            try:
                cleaned_text = ResponseParser._clean_invalid_escapes(response_text)
                data = json.loads(cleaned_text)

            except json.JSONDecodeError as second_error:
                # Double-check if the cleaned version was also truncated
                if is_truncation(second_error, cleaned_text):
                    raise ValueError(
                        "🛑 **Assessment Generation Incomplete**\n\n"
                        "The AI reached its maximum output limit before finishing all the questions.\n\n"
                        "💡 **Fix:** Please reduce the 'Total Questions' (try 5 to 10 at a time) and generate again."
                    ) from second_error

                raise ValueError(
                    f"⚠️ **Invalid AI Output Format**\n\n"
                    f"The AI generated a mathematical symbol or character that broke the JSON format.\n"
                    f"Error Details: {second_error}\n\n"
                    f"💡 **Fix:** Try clicking 'Generate' again to get a clean batch of questions."
                ) from second_error

        try:
            # Validate against Pydantic model
            return AssessmentOutput.model_validate(data)

        except Exception as error:
            raise ValueError(
                f"⚠️ **Validation Failed**\n\n"
                f"The AI missed a required field in the assessment structure.\n\n{error}"
            ) from error
