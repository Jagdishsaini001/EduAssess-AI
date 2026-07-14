"""
==============================================================================
EduAssess AI
------------------------------------------------------------------------------
Version : 0.5.2
Module  : Create Assessment
==============================================================================
"""

import streamlit as st

from models.assessment import Assessment
from prompts.assessment_prompt import build_assessment_prompt
from services.gemini_service import GeminiService
from core.response_parser import ResponseParser

# Import the updated syllabus dictionary
# Note: Ensure your syllabus file is named 'syllabus.py'
from data.syllabus import COMMERCE_SYLLABUS

st.set_page_config(
    page_title="Create Assessment",
    layout="wide",
)

st.title("📝 Create Assessment")

# =============================================================================
# Assessment Information
# =============================================================================

st.subheader("Assessment Information")

assessment_name = st.text_input(
    "Assessment Name",
    value="Punjab Lecturer Recruitment 2026 (Commerce)",
)

purpose = st.selectbox(
    "Purpose",
    [
        "Practice",
        "Quiz",
        "Assignment",
        "Mid-Term",
        "End-Term",
        "Competitive Exam",
        "Interview Preparation",
    ],
    index=5,
)

# =============================================================================
# Academic Information (Updated with Cascading Dropdowns)
# =============================================================================

st.subheader("Academic Information")

programme = st.selectbox(
    "Programme",
    [
        "Commerce",
        "Undergraduate",
        "Postgraduate",
        "MBA",
        "School",
        "Engineering",
        "Corporate Training",
        "Other",
    ],
    index=0,
)

semester = st.text_input(
    "Semester",
    value="N/A",
)

course = st.text_input(
    "Course",
    value="Punjab Lecturer Recruitment 2026",
)

# 1. Subject Dropdown
subject_options = list(COMMERCE_SYLLABUS.keys())
subject = st.selectbox(
    "Subject",
    options=subject_options,
)

# 2. Chapter Dropdown (Updates dynamically based on selected Subject)
if subject:
    chapter_options = list(COMMERCE_SYLLABUS[subject].keys())
else:
    chapter_options = []

chapter = st.selectbox(
    "Chapter",
    options=chapter_options,
)

# 3. Topic Dropdown (Updates dynamically based on selected Chapter)
if subject and chapter:
    topic_options = COMMERCE_SYLLABUS[subject][chapter].get("topics", [])
else:
    topic_options = []

topic = st.selectbox(
    "Topic",
    options=topic_options,
)

# =============================================================================
# Assessment Blueprint
# =============================================================================

st.subheader("Assessment Blueprint")

mcq = st.number_input(
    "MCQ",
    min_value=1,
    value=20,
)

true_false = st.number_input(
    "True / False",
    min_value=0,
    value=0,
)

assertion_reason = st.number_input(
    "Assertion-Reason",
    min_value=0,
    value=0,
)

case_mcq = st.number_input(
    "Case-based MCQ",
    min_value=0,
    value=0,
)

numerical_mcq = st.number_input(
    "Numerical MCQ",
    min_value=0,
    value=0,
)

total_questions = mcq + true_false + assertion_reason + case_mcq + numerical_mcq

st.success(f"Total Questions : {total_questions}")

# =============================================================================
# AI Settings
# =============================================================================

st.subheader("AI Settings")

knowledge = st.radio(
    "Knowledge Source",
    [
        "Uploaded Resources",
        "AI Knowledge",
        "Hybrid (Recommended)",
    ],
    index=2,
)

with st.expander("Advanced Settings"):

    bloom = st.selectbox(
        "Bloom Level",
        [
            "Remember",
            "Understand",
            "Apply",
            "Analyse",
            "Evaluate",
            "Create",
        ],
        index=2,
    )

    ai_mode = st.selectbox(
        "AI Behaviour",
        [
            "Strict",
            "Balanced",
            "Creative",
        ],
        index=1,
    )

    shuffle_questions = st.checkbox(
        "Shuffle Questions",
        value=True,
    )

    shuffle_options = st.checkbox(
        "Shuffle Options",
        value=True,
    )

    instructions = st.text_area(
        "Additional Instructions",
        value="Generate high quality Commerce questions suitable for Punjab Lecturer Recruitment 2026.",
    )

st.divider()

# =============================================================================
# Generate Assessment
# =============================================================================

if st.button(
    "🚀 Generate Assessment",
    use_container_width=True,
):

    try:

        request = Assessment(
            assessment_name=assessment_name,
            purpose=purpose,
            programme=programme,
            semester=semester,
            course=course,
            subject=subject,
            chapter=chapter,
            topic=topic,
            knowledge_source=knowledge,
            bloom_level=bloom,
            ai_behaviour=ai_mode,
            additional_instructions=instructions,
            question_blueprint={
                "MCQ": mcq,
                "True/False": true_false,
                "Assertion-Reason": assertion_reason,
                "Case-based MCQ": case_mcq,
                "Numerical MCQ": numerical_mcq,
            },
        )

        prompt = build_assessment_prompt(request)

        with st.spinner("Generating assessment using Gemini..."):

            service = GeminiService()

            response = service.generate(prompt)

            assessment = ResponseParser.parse(response)

        st.session_state["assessment"] = assessment

        st.success("Assessment generated successfully.")

    except Exception as error:

        st.error(str(error))

# =============================================================================
# Display Generated Assessment
# =============================================================================

assessment = st.session_state.get("assessment")

if assessment is not None:

    st.divider()

    st.header(assessment.assessment_name)

    st.write(f"**Subject:** {assessment.subject}")
    st.write(f"**Chapter:** {assessment.chapter}")
    st.write(f"**Topic:** {assessment.topic}")

    st.info(f"Total Questions : {len(assessment.questions)}")

    st.warning(
        "Preview only. "
        "Correct answers and explanations "
        "will be shown after submitting the assessment."
    )

    st.info("The assessment is ready. " "Click **Attempt Assessment** to begin.")

    st.metric(
        "Total Questions",
        len(assessment.questions),
    )

    st.divider()

    if st.button(
        "➡️ Attempt Assessment",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page("pages/03_Attempt_Assessment.py")
