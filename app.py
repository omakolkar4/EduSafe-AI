import textwrap

import streamlit as st
from agent import generate_response


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EduSafe AI | Learning Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==================================================
# SESSION STATE
# ==================================================

if "academic_question" not in st.session_state:
    st.session_state.academic_question = ""

if "study_material" not in st.session_state:
    st.session_state.study_material = ""

if "latest_answer" not in st.session_state:
    st.session_state.latest_answer = ""

if "latest_is_warning" not in st.session_state:
    st.session_state.latest_is_warning = False


def clear_all():
    st.session_state.academic_question = ""
    st.session_state.study_material = ""
    st.session_state.latest_answer = ""
    st.session_state.latest_is_warning = False


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background: #f5f8ff;
    color: #17233c;
}

/* Hide sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Header */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Main container */
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main heading */
.hero-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #173b78;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 16px;
    color: #64748b;
    margin-bottom: 22px;
}

/* Model status */
.status-pill {
    display: inline-block;
    background: #e8f1ff;
    color: #2457a6;
    border: 1px solid #d5e5ff;
    padding: 8px 14px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
}

/* Welcome banner */
.welcome-banner {
    background: linear-gradient(110deg, #173f80, #3478dc);
    padding: 28px 30px;
    border-radius: 16px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 8px 22px rgba(35, 85, 160, 0.12);
}

.welcome-title {
    font-size: 25px;
    font-weight: 750;
    margin-bottom: 8px;
}

.welcome-description {
    font-size: 15px;
    opacity: 0.94;
}

/* Section headings */
.section-heading {
    color: #18396e;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 6px;
}

.section-description {
    color: #718096;
    font-size: 14px;
    margin-bottom: 14px;
}

/* Input containers */
div[data-testid="stTextArea"] {
    background: #ffffff;
    border: 1px solid #e1e9f5;
    border-radius: 13px;
    padding: 10px;
    box-shadow: 0 3px 12px rgba(35, 65, 110, 0.035);
}

/* Text areas */
.stTextArea textarea {
    background: #fbfcff !important;
    color: #17233c !important;
    border: 1px solid #dce5f2 !important;
    border-radius: 9px !important;
    font-size: 15px !important;
    padding: 13px !important;
}

.stTextArea textarea:focus {
    border: 1px solid #3979df !important;
    box-shadow: 0 0 0 2px rgba(57, 121, 223, 0.10) !important;
}

/* Hide text area labels */
.stTextArea label {
    color: #344563 !important;
    font-weight: 600 !important;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    height: 48px;
    font-size: 15px;
    font-weight: 650;
    transition: all 0.2s ease;
}

/* Primary button */
.stButton > button[kind="primary"] {
    background: #2864c5;
    color: white;
    border: 1px solid #2864c5;
}

.stButton > button[kind="primary"]:hover {
    background: #174c9f;
    border-color: #174c9f;
    color: white;
}

/* Secondary button */
.stButton > button[kind="secondary"] {
    background: white;
    color: #35547e;
    border: 1px solid #d5e0ef;
}

.stButton > button[kind="secondary"]:hover {
    background: #edf4ff;
    border-color: #9bbce9;
    color: #173b78;
}

/* Response card */
.response-card {
    background: white;
    border: 1px solid #dfe8f5;
    border-left: 5px solid #3478dc;
    border-radius: 13px;
    padding: 23px;
    margin-top: 12px;
    color: #253653;
    line-height: 1.8;
    box-shadow: 0 4px 16px rgba(35, 65, 110, 0.04);
}

/* Footer */
.footer {
    text-align: center;
    color: #8793a7;
    font-size: 12px;
    margin-top: 42px;
    padding: 20px;
    border-top: 1px solid #e4eaf4;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .hero-title {
        font-size: 32px;
    }

    .welcome-banner {
        padding: 20px;
    }

    .welcome-title {
        font-size: 21px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

header_left, header_right = st.columns([3, 1])

with header_left:

    st.markdown(
        '<div class="hero-title">EduSafe AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'A smarter and safer way to learn with artificial intelligence.'
        '</div>',
        unsafe_allow_html=True
    )

with header_right:

    st.markdown(
        '<div style="text-align:right; padding-top:15px;">'
        '<span class="status-pill">● Local AI · Qwen 2.5 3B</span>'
        '</div>',
        unsafe_allow_html=True
    )


st.divider()


# ==================================================
# WELCOME BANNER
# ==================================================

welcome_html = """
<div class="welcome-banner">
    <div class="welcome-title">
        Welcome to your learning space.
    </div>
    <div class="welcome-description">
        Ask questions, understand difficult concepts, and learn
        from your study material with AI-powered assistance.
    </div>
</div>
"""

st.markdown(
    textwrap.dedent(welcome_html),
    unsafe_allow_html=True
)


# ==================================================
# QUESTION INPUT
# ==================================================

st.markdown("""
<div class="section-heading">
    Ask your question
</div>

<div class="section-description">
    Enter an academic question and let EduSafe AI help you understand it.
</div>
""", unsafe_allow_html=True)


question = st.text_area(
    "Your question",
    placeholder=(
        "For example: Explain Machine Learning in simple words..."
    ),
    height=120,
    max_chars=2000,
    label_visibility="collapsed",
    key="academic_question"
)


# ==================================================
# STUDY MATERIAL INPUT
# ==================================================

st.markdown("""
<div class="section-heading" style="margin-top:22px;">
    Add study material
    <span style="
        font-size:12px;
        color:#8290a5;
        font-weight:500;
    ">(Optional)</span>
</div>

<div class="section-description">
    Paste your notes or learning material to give the AI additional context.
</div>
""", unsafe_allow_html=True)


study_material = st.text_area(
    "Study material",
    placeholder=(
        "Paste your class notes, textbook content, "
        "or study material here..."
    ),
    height=170,
    label_visibility="collapsed",
    key="study_material"
)


st.caption(
    "Your supplied material is checked for potentially malicious "
    "instructions before being processed."
)


# ==================================================
# ACTION BUTTONS
# ==================================================

st.write("")

generate_col, clear_col = st.columns([4, 1])

with generate_col:

    generate_clicked = st.button(
        "Generate Answer  →",
        type="primary",
        use_container_width=True
    )

with clear_col:

    st.button(
        "Clear All",
        type="secondary",
        use_container_width=True,
        on_click=clear_all
    )


# ==================================================
# GENERATE AI RESPONSE
# ==================================================

if generate_clicked:

    if not question.strip():

        st.warning("Please enter an academic question first.")

    else:

        with st.spinner(
            "EduSafe AI is checking your request and preparing an answer..."
        ):

            answer = generate_response(
                question,
                study_material
            )

        st.session_state.latest_answer = answer

        st.session_state.latest_is_warning = (
            "blocked" in answer.lower()
            or "protection:" in answer.lower()
            or "warning:" in answer.lower()
            or "unable to generate" in answer.lower()
        )


# ==================================================
# AI RESPONSE DISPLAY
# ==================================================

if st.session_state.latest_answer:

    st.divider()

    st.markdown("""
    <div class="section-heading">
        Your AI response
    </div>

    <div class="section-description">
        Generated by EduSafe AI using your local language model.
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.latest_is_warning:

        st.error(st.session_state.latest_answer)

    else:

        st.markdown(
            '<div class="response-card">',
            unsafe_allow_html=True
        )

        st.markdown(st.session_state.latest_answer)

        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================

footer_html = """
<div class="footer">
    <b>EduSafe AI</b> · Educational AI Assistant
    <br>
    Built with Python, Streamlit, LangChain and Ollama
    <br><br>
    AI-powered learning with responsible safety controls.
</div>
"""

st.markdown(
    textwrap.dedent(footer_html),
    unsafe_allow_html=True
)