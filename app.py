"""
==============================================================================
EduAssess AI
------------------------------------------------------------------------------
Version : 0.5.0
Application : Home
Target      : Punjab Lecturer Recruitment 2026 (Commerce)
==============================================================================
"""

import streamlit as st

st.set_page_config(
    page_title="EduAssess AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# Session Initialization
# =============================================================================

st.session_state.setdefault("assessment", None)
st.session_state.setdefault("answers", {})
st.session_state.setdefault("results", None)
st.session_state.setdefault("score", None)
st.session_state.setdefault("total_questions", None)

# =============================================================================
# Header
# =============================================================================

st.title("🎓 EduAssess AI")

st.subheader(
    "AI-Powered Assessment Generator for Punjab Lecturer Recruitment 2026 (Commerce)"
)

st.markdown(
    """
Generate high-quality Commerce assessments using Google Gemini,
attempt the assessment, receive instant scoring,
and review detailed explanations.
"""
)

st.divider()

# =============================================================================
# Features
# =============================================================================

st.header("Features")

col1, col2 = st.columns(2)

with col1:

    st.success("✅ AI Question Generation")

    st.success("✅ Multiple Question Types")

    st.success("✅ Lecturer Recruitment Focus")

    st.success("✅ Bloom's Taxonomy Support")

with col2:

    st.success("✅ Instant Assessment")

    st.success("✅ Automatic Scoring")

    st.success("✅ Detailed Explanations")

    st.success("✅ Review Incorrect Answers")

st.divider()

# =============================================================================
# Workflow
# =============================================================================

st.header("Workflow")

st.markdown(
    """
1. **Create Assessment**
   - Choose subject, chapter and topic.
   - Configure question blueprint.
   - Generate assessment using Gemini.

2. **Attempt Assessment**
   - Answer all questions.
   - Submit when complete.

3. **View Results**
   - Instant score.
   - Percentage.
   - Correct answers.

4. **Review**
   - Read explanations.
   - Analyse mistakes.
   - Improve performance.
"""
)

st.divider()

# =============================================================================
# Launch Buttons
# =============================================================================

st.header("Get Started")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "📝 Create Assessment",
        use_container_width=True,
    ):
        st.switch_page("pages/02_Create_Assessment.py")

with col2:

    if st.button(
        "🚀 Attempt Latest Assessment",
        use_container_width=True,
        disabled=st.session_state["assessment"] is None,
    ):
        st.switch_page("pages/03_Attempt_Assessment.py")

st.divider()

# =============================================================================
# Current Session
# =============================================================================

st.header("Current Session")

assessment_loaded = st.session_state["assessment"] is not None
results_available = st.session_state["results"] is not None

status_col1, status_col2 = st.columns(2)

with status_col1:

    if assessment_loaded:
        st.success("Assessment Loaded")
    else:
        st.info("No Assessment Loaded")

with status_col2:

    if results_available:
        st.success("Results Available")
    else:
        st.info("No Results Available")

st.divider()

# =============================================================================
# Footer
# =============================================================================

st.caption(
    "EduAssess AI • MVP Launch • Google Gemini • Streamlit • Pydantic"
)