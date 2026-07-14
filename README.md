# 🎓 EduAssess AI

AI-powered assessment generation and evaluation platform built with **Streamlit**, **Google Gemini**, and **Pydantic**.

Current MVP focuses on **Punjab Lecturer Recruitment 2026 (Commerce)**.

---

# Features

- AI-generated Commerce questions
- Multiple assessment types
- Structured JSON output
- Automatic validation using Pydantic
- Interactive online test
- Instant scoring
- Detailed explanations
- Review mode

---

# Technology Stack

- Python 3.11+
- Streamlit
- Google Gemini (google-genai SDK)
- Pydantic v2
- python-dotenv

---

# Project Structure

```
EduAssessAI/
│
├── app.py
├── config.py
├── requirements.txt
│
├── models/
│   ├── assessment.py
│   ├── assessment_output.py
│   └── question.py
│
├── prompts/
│   └── assessment_prompt.py
│
├── services/
│   └── gemini_service.py
│
├── core/
│   └── response_parser.py
│
├── pages/
│   ├── 02_Create_Assessment.py
│   ├── 03_Attempt_Assessment.py
│   ├── 04_Results.py
│   └── 05_Review.py
│
└── .env
```

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
cd EduAssessAI
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Configure Gemini

Create a `.env` file.

```text
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Workflow

1. Open the application.
2. Create an assessment.
3. Generate questions using Gemini.
4. Attempt the assessment.
5. Submit answers.
6. View score.
7. Review explanations.

---

# Current MVP Scope

- Generate Questions
- Attempt Assessment
- Automatic Scoring
- Detailed Explanations

---

# Output Format

Gemini returns structured JSON validated against the Pydantic models.

Main models:

- Assessment
- AssessmentOutput
- Question

---

# Target Audience

Punjab Lecturer Recruitment 2026 (Commerce)

---

# Version

**EduAssess AI v0.5.0 (MVP Launch)**

---

# License

For educational and research purposes.
