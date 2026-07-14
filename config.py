"""
==============================================================================
EduAssess AI
------------------------------------------------------------------------------
Version : 0.6.0
Module  : Configuration
==============================================================================
"""

import os

from dotenv import load_dotenv

# =============================================================================
# Load Environment Variables
# =============================================================================

load_dotenv(override=True)

# =============================================================================
# Gemini API Keys
# =============================================================================

GEMINI_API_KEYS = [
    os.getenv("GEMINI_API_KEY_1", "").strip(),
    os.getenv("GEMINI_API_KEY_2", "").strip(),
    os.getenv("GEMINI_API_KEY_3", "").strip(),
]

# Remove empty keys

GEMINI_API_KEYS = [key for key in GEMINI_API_KEYS if key]

# =============================================================================
# Gemini Model
# =============================================================================

MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.5-flash",
).strip()

# =============================================================================
# Application
# =============================================================================

APP_NAME = "EduAssess AI"

APP_VERSION = "0.6.0"

TARGET_EXAM = "Punjab Lecturer Recruitment 2026 (Commerce)"

# =============================================================================
# Validation
# =============================================================================

if not GEMINI_API_KEYS:

    raise ValueError(
        "No Gemini API Keys found.\n\n"
        "Please configure at least one API key in your .env file."
    )
