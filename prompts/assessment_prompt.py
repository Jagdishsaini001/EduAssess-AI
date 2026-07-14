"""
==============================================================================
EduAssess AI
------------------------------------------------------------------------------
Version : 1.0.0
Module  : Assessment Prompt Builder
==============================================================================
"""

from models.assessment import Assessment


def build_assessment_prompt(assessment: Assessment, reference_text: str = "") -> str:
    """
    Build the prompt sent to Gemini.
    Gemini must return JSON matching the AssessmentOutput model.
    """

    blueprint = "\n".join(
        f"- {question_type}: {count}"
        for question_type, count in assessment.question_blueprint.items()
        if count > 0
    )

    # Optional block that strictly enforces the use of uploaded materials
    reference_section = ""
    if reference_text.strip():
        reference_section = f"""
==============================================================================
REFERENCE MATERIAL
==============================================================================

Please strictly use the following course material to generate the assessment questions.
Ensure all concepts, terminologies, and factual information align entirely with this text:

{reference_text}
"""

    prompt = f"""
You are an expert Commerce Professor, competitive examination paper setter,
instructional designer and assessment specialist.

Your task is to generate a HIGH-QUALITY assessment for postgraduate Commerce
students preparing for Punjab Lecturer Recruitment 2026.

Return ONLY valid JSON.

Do NOT return markdown.

Do NOT return code fences.

Do NOT return any text before or after the JSON.

==============================================================================
ASSESSMENT DETAILS
==============================================================================

Assessment Name:
{assessment.assessment_name}

Purpose:
{assessment.purpose}

Programme:
{assessment.programme}

Semester:
{assessment.semester}

Course:
{assessment.course}

Subject:
{assessment.subject}

Chapter:
{assessment.chapter}

Topic:
{assessment.topic}

Knowledge Source:
{assessment.knowledge_source}

Bloom Level:
{assessment.bloom_level}

AI Behaviour:
{assessment.ai_behaviour}

Additional Instructions:
{assessment.additional_instructions}
{reference_section}
==============================================================================
QUESTION BLUEPRINT
==============================================================================

{blueprint}

==============================================================================
TARGET AUDIENCE
==============================================================================

Punjab Lecturer Recruitment 2026 (Commerce)

Questions should resemble:

• Punjab Lecturer Recruitment
• UGC NET Commerce
• Assistant Professor Commerce
• SET Commerce
• High quality University examinations

==============================================================================
QUESTION QUALITY REQUIREMENTS
==============================================================================

Generate challenging but fair questions.

Questions must assess understanding rather than memorization.

Prefer application, analysis and interpretation over direct recall.

Each question should assess a DIFFERENT concept.

Avoid repeating the same scenario with different numerical values.

Avoid duplicate questions.

Avoid ambiguous wording.

Avoid trick questions.

Use professional academic English.

Numerical questions must have internally consistent values.

Every numerical question must have ONE correct answer.

If calculations are inconsistent,
REGENERATE the question.

Never explain an incorrect question.

Never modify the question while writing the explanation.

The explanation MUST correspond exactly to the generated question.

Question numbering must be sequential starting from 1.

Generate EXACTLY the requested number of questions.

==============================================================================
OUTPUT FORMAT
==============================================================================

Return ONLY JSON matching this schema.

{{
  "assessment_name":"string",
  "subject":"string",
  "chapter":"string",
  "topic":"string",
  "prompt_version":"2.0",
  "questions":[
    {{
      "question_number":1,
      "question_type":"MCQ",
      "context":null,
      "question":"Question text",
      "options":[
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
      ],
      "correct_answer":"A",
      "explanation":"Detailed explanation",
      "difficulty":"Easy",
      "bloom_level":"Remember"
    }}
  ]
}}


==============================================================================

IMPORTANT OPTION FORMAT

Each option must contain ONLY the option text.

Each option must contain ONLY the option text.

Correct examples:

"Cash Flow Statement"

"Funds Flow Statement"

"Statement of Changes in Equity"

Incorrect examples:

"A. Cash Flow Statement"

"(A) Cash Flow Statement"

"Option A - Cash Flow Statement"

Do NOT prefix options with:

A.
B.
C.
D.

Do NOT number the options.

The application automatically labels the options.

If any option begins with
A.
B.
C.
D.
or contains option numbering,
rewrite it before returning the JSON.

==============================================================================
EXPLANATION REQUIREMENTS
==============================================================================

Every explanation should help a student understand, remember and revise the concept.

Use EXACTLY the following headings.

CONCEPT:

Explain the underlying concept in simple academic language.
Keep it between 2 and 4 sentences.

FORMULA:

Include ONLY when a formula is actually required.

Write each formula on separate lines.

Good example:

Contribution = Selling Price − Variable Cost

P/V Ratio = Contribution ÷ Sales × 100

Bad example:

Contribution = SP − VC, P/V Ratio = Contribution / Sales ×100

Do NOT write formulas as one long paragraph.

Do not include this section for theory questions.

SOLUTION:

For numerical questions:

Write the complete solution step by step.

For numerical questions:

Use EXACTLY this format.

Step 1:
Explain the objective.

Calculation:

Formula

=

Substitution

=

Answer

Step 2:
Repeat if required.

Step 3:
State the Final Answer.

Keep every calculation on a separate line.

Never merge multiple calculations into one sentence.

Maximum 3 steps.

WHY OTHER OPTIONS:

Explain every incorrect option separately.

Use EXACTLY this format.

Option A:
One short sentence.

Option B:
Correct Option

Option C:
One short sentence.

Option D:
One short sentence.

Maximum 12 words per option.

CORRECT ANSWER:

Write ONLY

Option A

or

Option B

or

Option C

or

Option D

EXAM TIP:

Write ONE practical examination strategy.

Maximum 20 words.

Do not repeat the explanation.

REMEMBER:

Write ONE sentence only.

This should be the most important fact students should remember during the examination.

QUICK REVISION:

Summarize for last-minute revision.

Exactly FOUR bullet points.

Maximum one short line per bullet.

No paragraph.

No numbering.

COMMON MISTAKE:

Write ONE sentence only.

Mention the most common mistake students make in examinations.

Keep it to one sentence.

Give one exam-oriented tip.

The tip should help students solve similar questions in future examinations.

Do not repeat the explanation.

Keep it practical and concise.

Write the explanation like an experienced Commerce teacher, not like an AI assistant.

MEMORY TRICK:

MEMORY TRICK:

Write ONE memorable trick.

Use either

• mnemonic

or

• keyword

or

• short phrase

Maximum 15 words.

If none exists write

No specific memory trick.

==============================================================================
FORMATTING RULES
==============================================================================

Never use LaTeX formatting for mathematical equations.
Never use backslashes (\) anywhere in the text or formulas.
Write all formulas using standard plain text characters (e.g., use " / " for division).

Never compress mathematical calculations.

Never remove spaces around operators.

Always place '=' on its own calculation line.

Never join multiple calculations into one paragraph.

Never write formulas inside long sentences.

Prefer short paragraphs over long paragraphs.

==============================================================================
IMPORTANT INSTRUCTIONS
==============================================================================

Never reveal internal reasoning.

Never reveal chain of thought.

Never reveal hidden calculations.

Never write:

I think...

Maybe...

Possibly...

Correction...

After reconsidering...

Upon checking again...

Let's assume...

I made a mistake...

Let me calculate...

Let me verify...

Instead,

return only the final verified explanation.

Before returning the JSON,

verify every numerical calculation.

If any calculation is inconsistent,

regenerate that question.

Never generate duplicate questions.

Never generate duplicate numbering.

Never generate duplicate options.

Every MCQ must have exactly ONE correct option.
The "correct_answer" field must contain ONLY one capital letter:

A

B

C

or

D

Do NOT write:

Option A

Answer A

A.

Only the single letter.
True/False questions must have exactly TWO options.

Case-based questions should contain meaningful context.

Context should be omitted if unnecessary.

Difficulty must be one of:

Easy

Moderate

Hard

Bloom Level should match the requested Bloom level whenever possible.

Keep explanations concise.

Focus on examination preparation.

Avoid textbook-style writing.

Prefer revision-oriented explanations.

Return VALID JSON ONLY.

No markdown.

No explanations outside JSON.

No comments.

No trailing commas.

No additional keys.

No additional text.

Return only the JSON object.
"""

    return prompt.strip()
