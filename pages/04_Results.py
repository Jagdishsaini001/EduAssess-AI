"""
==============================================================================
EduAssess AI
------------------------------------------------------------------------------
Version : 0.5.0
Module  : Results
==============================================================================
"""

import streamlit as st

st.set_page_config(
    page_title="Assessment Results",
    layout="wide",
)

st.title("📊 Assessment Results")

# =============================================================================
# Validate Session
# =============================================================================

if (
    "results" not in st.session_state
    or "score" not in st.session_state
    or "total_questions" not in st.session_state
):

    st.warning("No assessment results found.")
    st.stop()

results = st.session_state["results"]
score = st.session_state["score"]
total_questions = st.session_state["total_questions"]

percentage = (score / total_questions) * 100 if total_questions > 0 else 0

# =============================================================================
# Summary
# =============================================================================

st.subheader("Performance Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Score",
        f"{score}/{total_questions}",
    )

with col2:
    st.metric(
        "Percentage",
        f"{percentage:.2f}%",
    )

with col3:

    if percentage >= 80:
        grade = "Excellent"

    elif percentage >= 60:
        grade = "Good"

    elif percentage >= 40:
        grade = "Average"

    else:
        grade = "Needs Improvement"

    st.metric(
        "Performance",
        grade,
    )

st.progress(percentage / 100)

st.divider()

# =============================================================================
# Question Review
# =============================================================================

option_labels = ["A", "B", "C", "D"]

st.header("Question Review")

for item in results:

    st.subheader(f"Question {item['question_number']}")

    if item["is_correct"]:
        st.success("✅ Correct")
    else:
        st.error("❌ Incorrect")

    if item["context"]:

        if str(item["context"]).strip():

            st.info(item["context"])

    st.markdown(f"**{item['question']}**")

    for index, option in enumerate(item["options"]):

        if index < len(option_labels):
            label = option_labels[index]
        else:
            label = chr(65 + index)

        text = f"{label}. {option}"

        if label == item["correct_answer"]:
            text += " ✅"

        elif label == item["user_answer"]:
            text += " ❌"

        st.markdown(text)

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Your Answer:** {item['user_answer'] or 'Not Attempted'}")

    with col2:
        correct_option = ord(item["correct_answer"]) - 65
        st.write(
            f"**Correct Answer:** "
            f"{item['correct_answer']}. "
            f"{item['options'][correct_option]}"
        )

    with st.expander(
        "📘 View Explanation",
        expanded=False,
    ):

        st.markdown(item["explanation"])

        col1, col2 = st.columns(2)

        with col1:
            st.caption(f"Difficulty: {item['difficulty']}")

        with col2:
            st.caption(f"Bloom Level: {item['bloom_level']}")

    st.divider()

# =============================================================================
# Actions
# =============================================================================

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🔄 Attempt Again",
        use_container_width=True,
    ):

        st.session_state.pop("answers", None)
        st.session_state.pop("results", None)
        st.session_state.pop("score", None)
        st.session_state.pop("total_questions", None)

        st.switch_page("pages/03_Attempt_Assessment.py")

with col2:

    if st.button(
        "📝 Create New Assessment",
        use_container_width=True,
    ):

        st.session_state.pop("assessment", None)
        st.session_state.pop("answers", None)
        st.session_state.pop("results", None)
        st.session_state.pop("score", None)
        st.session_state.pop("total_questions", None)

        st.switch_page("pages/02_Create_Assessment.py")
