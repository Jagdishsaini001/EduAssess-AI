"""
==============================================================================
EduAssess AI
------------------------------------------------------------------------------
Version : 0.5.0
Module  : Attempt Assessment
==============================================================================
"""

import streamlit as st

st.set_page_config(
    page_title="Attempt Assessment",
    layout="wide",
)

st.title("📝 Attempt Assessment")

# =============================================================================
# Validate Assessment
# =============================================================================

if "assessment" not in st.session_state:

    st.warning("No assessment found. Please create an assessment first.")
    st.stop()

assessment = st.session_state["assessment"]

# =============================================================================
# Initialize Session State
# =============================================================================

if "answers" not in st.session_state:

    st.session_state["answers"] = {}

# =============================================================================
# Assessment Header
# =============================================================================

st.subheader(assessment.assessment_name)

st.write(f"**Subject:** {assessment.subject}")
st.write(f"**Chapter:** {assessment.chapter}")
st.write(f"**Topic:** {assessment.topic}")

st.divider()

option_labels = ["A", "B", "C", "D"]

# =============================================================================
# Display Questions
# =============================================================================

for question in assessment.questions:

    st.markdown(f"### Question {question.question_number}")

    if question.context:

        if question.context.strip():

            st.info(question.context)

    st.write(question.question)

    radio_options = []

    for index, option in enumerate(question.options):

        if index < len(option_labels):
            label = option_labels[index]
        else:
            label = chr(65 + index)

        radio_options.append(f"{label}. {option}")

    answer = st.radio(
        "Select your answer",
        radio_options,
        key=f"q_{question.question_number}",
        index=None,
    )

    if answer:

       selected_option = answer.split(".", 1)[0]
       
       st.session_state["answers"][question.question_number] = selected_option

    st.divider()

# =============================================================================
# Submit
# =============================================================================

if st.button(
    "✅ Submit Assessment",
    use_container_width=True,
):

    answers = st.session_state["answers"]

    score = 0

    results = []

    for question in assessment.questions:

        user_answer = answers.get(question.question_number)

        is_correct = user_answer == question.correct_answer

        if is_correct:
            score += 1

        results.append(
            {
                "question_number": question.question_number,
                "question": question.question,
                "context": question.context,
                "options": question.options,
                "correct_answer": question.correct_answer,
                "user_answer": user_answer,
                "explanation": question.explanation,
                "difficulty": question.difficulty,
                "bloom_level": question.bloom_level,
                "is_correct": is_correct,
            }
        )

    st.session_state["score"] = score

    st.session_state["total_questions"] = len(assessment.questions)

    st.session_state["results"] = results

    st.switch_page("pages/04_Results.py")