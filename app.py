import streamlit as st
from workflow.blog_workflow import blog_workflow


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="BlogForge AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# DARK UI CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
       ====================================================== */

    html, body, [data-testid="stAppViewContainer"],
    [data-testid="stApp"] {
        background: #05070d !important;
        color: #ffffff !important;
    }

    [data-testid="stHeader"] {
        background: #05070d !important;
    }

    [data-testid="stToolbar"] {
        background: #05070d !important;
    }

    .main {
        background: #05070d !important;
    }

    .block-container {
        max-width: 1250px !important;
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
    }


    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {
        background: #080b12 !important;
        border-right: 1px solid #1d2433 !important;
    }

    section[data-testid="stSidebar"] > div {
        background: #080b12 !important;
    }

    section[data-testid="stSidebar"] .block-container {
        padding: 2rem 1.35rem !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label {
        color: #ffffff !important;
    }


    /* ======================================================
       SIDEBAR BRAND
       ====================================================== */

    .brand {
        font-size: 30px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 4px;
    }

    .brand-subtitle {
        color: #8fa4c7;
        font-size: 14px;
        margin-bottom: 28px;
    }

    .divider {
        height: 1px;
        background: #202838;
        margin: 24px 0 28px 0;
    }


    /* ======================================================
       SIDEBAR SELECT BOX
       ====================================================== */

    section[data-testid="stSidebar"]
    div[data-baseweb="select"] > div {

        background: #111722 !important;

        border: 1px solid #283247 !important;

        border-radius: 10px !important;

        color: #ffffff !important;

        min-height: 46px !important;

        box-shadow: none !important;
    }

    section[data-testid="stSidebar"]
    div[data-baseweb="select"] > div:hover {

        border-color: #7c5cff !important;

        background: #151b29 !important;
    }

    section[data-testid="stSidebar"]
    div[data-baseweb="select"] span {

        color: #ffffff !important;

        background: transparent !important;
    }

    section[data-testid="stSidebar"]
    div[data-baseweb="select"] svg {

        fill: #94a3b8 !important;

        color: #94a3b8 !important;
    }


    /* ======================================================
       DROPDOWN
       ====================================================== */

    div[data-baseweb="popover"] {
        background: #0c111b !important;
    }

    div[role="listbox"] {
        background: #0c111b !important;
        border: 1px solid #273044 !important;
    }

    div[role="option"] {
        background: #0c111b !important;
        color: #ffffff !important;
    }

    div[role="option"]:hover {
        background: #1a2232 !important;
    }


    /* ======================================================
       SIDEBAR LABELS
       ====================================================== */

    section[data-testid="stSidebar"] label {

        color: #dbe4f2 !important;

        font-size: 13px !important;

        font-weight: 600 !important;
    }


    /* ======================================================
       PIPELINE TITLE
       ====================================================== */

    .pipeline-heading {

        color: #ffffff;

        font-size: 20px;

        font-weight: 750;

        margin-bottom: 16px;
    }


    /* ======================================================
       PIPELINE CARD
       ====================================================== */

    .pipeline-card {

        background: #0d131f;

        border: 1px solid #202b3e;

        border-radius: 12px;

        padding: 12px 14px;

        margin-bottom: 9px;

        transition: all 0.2s ease;
    }

    .pipeline-card:hover {

        border-color: #5141a8;

        background: #111827;
    }

    .pipeline-name {

        color: #f8fafc;

        font-size: 14px;

        font-weight: 650;
    }

    .pipeline-status {

        color: #64748b;

        font-size: 12px;

        margin-top: 3px;
    }


    /* ======================================================
       HERO
       ====================================================== */

    .hero-space {
        height: 25px;
    }


    /* ======================================================
       TEXT AREA
       ====================================================== */

    textarea {

        background: #090e17 !important;

        color: #ffffff !important;

        border: 1px solid #303b50 !important;

        border-radius: 14px !important;

        font-size: 16px !important;

        padding: 18px !important;
    }

    textarea::placeholder {

        color: #64748b !important;
    }

    textarea:focus {

        border-color: #8b5cf6 !important;

        box-shadow:
            0 0 0 1px #8b5cf6,
            0 0 25px rgba(139, 92, 246, 0.12) !important;
    }


    /* ======================================================
       GENERATE BUTTON
       ====================================================== */

    div.stButton > button {

        width: 100% !important;

        height: 56px !important;

        border: none !important;

        border-radius: 13px !important;

        background:
            linear-gradient(
                90deg,
                #5b5ff0,
                #8b5cf6
            ) !important;

        color: white !important;

        font-size: 16px !important;

        font-weight: 700 !important;

        box-shadow:
            0 8px 30px
            rgba(99, 102, 241, 0.18) !important;

        transition: all 0.2s ease !important;
    }

    div.stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 12px 35px
            rgba(139, 92, 246, 0.28) !important;
    }


    /* ======================================================
       ALERTS
       ====================================================== */

    div[data-testid="stAlert"] {

        background: #0d1420 !important;

        border: 1px solid #263248 !important;

        color: #ffffff !important;
    }


    /* ======================================================
       PROGRESS
       ====================================================== */

    div[data-testid="stProgress"] > div {

        background: #161d2b !important;

        border-radius: 10px !important;
    }

    div[data-testid="stProgress"] > div > div {

        background:
            linear-gradient(
                90deg,
                #6366f1,
                #8b5cf6
            ) !important;

        border-radius: 10px !important;
    }


    /* ======================================================
       METRIC
       ====================================================== */

    div[data-testid="stMetric"] {

        background: #0c121d !important;

        border: 1px solid #202b3e !important;

        border-radius: 14px !important;

        padding: 18px !important;
    }

    div[data-testid="stMetricLabel"] {

        color: #8795aa !important;
    }

    div[data-testid="stMetricValue"] {

        color: #ffffff !important;
    }


    /* ======================================================
       BLOG RESULT
       ====================================================== */

    .blog-result {

        background: #0b111b;

        border: 1px solid #202b3e;

        border-radius: 16px;

        padding: 30px;

        margin-top: 20px;
    }


    /* ======================================================
       DOWNLOAD BUTTON
       ====================================================== */

    div[data-testid="stDownloadButton"] button {

        background: #111827 !important;

        color: #ffffff !important;

        border: 1px solid #303b50 !important;

        border-radius: 10px !important;
    }

    div[data-testid="stDownloadButton"] button:hover {

        border-color: #8b5cf6 !important;

        background: #151d2c !important;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    .footer-text {

        text-align: center;

        color: #526078;

        font-size: 12px;

        margin-top: 55px;

        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "generated_blog" not in st.session_state:
    st.session_state.generated_blog = ""

if "pipeline_status" not in st.session_state:

    st.session_state.pipeline_status = {
        "Research Agent": "Waiting",
        "Content Planner": "Waiting",
        "SEO Agent": "Waiting",
        "Writer Agent": "Waiting",
        "Reviewer Agent": "Waiting",
        "Editor Agent": "Waiting",
    }


# ============================================================
# PIPELINE
# ============================================================

PIPELINE_NODES = [

    ("🔎", "Research Agent"),

    ("📋", "Content Planner"),

    ("🔍", "SEO Agent"),

    ("✍️", "Writer Agent"),

    ("🧐", "Reviewer Agent"),

    ("🛠️", "Editor Agent"),
]


def reset_pipeline():

    st.session_state.pipeline_status = {

        "Research Agent": "Waiting",

        "Content Planner": "Waiting",

        "SEO Agent": "Waiting",

        "Writer Agent": "Waiting",

        "Reviewer Agent": "Waiting",

        "Editor Agent": "Waiting",
    }


def render_pipeline():

    st.markdown(
        "### 🧠 AI Pipeline"
    )

    for icon, name in PIPELINE_NODES:

        status = st.session_state.pipeline_status[name]

        if status == "Completed":

            st.markdown(
                f"""
                <div class="pipeline-card">
                    <div class="pipeline-name">
                        {icon} &nbsp; {name}
                    </div>
                    <div class="pipeline-status"
                         style="color:#34d399;">
                        ● Completed
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        elif status == "Running":

            st.markdown(
                f"""
                <div class="pipeline-card">
                    <div class="pipeline-name">
                        {icon} &nbsp; {name}
                    </div>
                    <div class="pipeline-status"
                         style="color:#a78bfa;">
                        ◉ Running
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="pipeline-card">
                    <div class="pipeline-name">
                        {icon} &nbsp; {name}
                    </div>
                    <div class="pipeline-status">
                        ○ Waiting
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 🤖 BlogForge"
    )

    st.markdown(
        '<div class="brand-subtitle">Multi-Agent AI Blog Generator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "### ⚙️ Generation Settings"
    )

    audience = st.selectbox(
        "Target audience",
        [
            "General readers",
            "Students",
            "Professionals",
            "Researchers",
            "Business leaders"
        ]
    )

    tone = st.selectbox(
        "Writing tone",
        [
            "Professional",
            "Conversational",
            "Educational",
            "Technical",
            "Friendly"
        ]
    )

    length = st.selectbox(
        "Article length",
        [
            "Short",
            "Medium",
            "Long"
        ],
        index=1
    )

    st.markdown(
        '<div class="divider"></div>',
        unsafe_allow_html=True
    )

    render_pipeline()


# ============================================================
# MAIN HERO
# ============================================================

st.markdown(
    "<div class='hero-space'></div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style="
        font-size: 58px;
        font-weight: 800;
        line-height: 1.1;
        color: #ffffff;
        margin-bottom: 18px;
    ">
        Turn ideas into
        <span style="color: #8b5cf6;">beautiful blogs.</span>
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        color: #8fa4c7;
        font-size: 17px;
        line-height: 1.7;
        max-width: 850px;
        margin-top: 0;
        margin-bottom: 35px;
    ">
        BlogForge researches your topic, plans your article,
        optimizes it for SEO, writes the content, reviews it,
        edits it, and produces a polished final article.
    </p>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TOPIC
# ============================================================

st.markdown(
    "## What do you want to write about?"
)

st.caption(
    "Give BlogForge a topic and let the AI pipeline do the work."
)

topic = st.text_area(
    "Blog topic",
    placeholder="Example: Impact of Artificial Intelligence on Education",
    height=145,
    label_visibility="collapsed"
)


# ============================================================
# GENERATE
# ============================================================

generate = st.button(
    "🚀  Generate My Blog",
    type="primary",
    use_container_width=True
)


# ============================================================
# GENERATION
# ============================================================

if generate:

    if not topic.strip():

        st.error(
            "Please enter a blog topic first.",
            icon="⚠️"
        )

    else:

        reset_pipeline()

        st.session_state.generated_blog = ""

        st.markdown(
            "## ⚡ BlogForge is generating your article..."
        )

        progress_bar = st.progress(
            0,
            text="Starting BlogForge..."
        )

        pipeline_placeholder = st.empty()
        

        initial_state = {
    "topic": topic.strip(),
    "audience": audience,
    "tone": tone,
    "length": length
}

        final_state = {}

        completed_count = 0

        node_order = [
            "research",
            "planner",
            "seo",
            "writer",
            "reviewer",
            "editor",
            "finalizer"
        ]

        try:

            for event in blog_workflow.stream(initial_state):

                for node_name, state_update in event.items():

                    if state_update:
                        final_state.update(state_update)

                    agent_map = {

                        "research":
                            "Research Agent",

                        "planner":
                            "Content Planner",

                        "seo":
                            "SEO Agent",

                        "writer":
                            "Writer Agent",

                        "reviewer":
                            "Reviewer Agent",

                        "editor":
                            "Editor Agent",
                    }

                    if node_name in agent_map:

                        agent_name = agent_map[node_name]

                        st.session_state.pipeline_status[
                            agent_name
                        ] = "Completed"

                        completed_count += 1

                    if node_name in node_order:

                        progress_value = min(
                            completed_count / 6,
                            1.0
                        )

                        progress_bar.progress(
                            progress_value,
                            text=f"{node_name.title()} completed..."
                        )

                    with pipeline_placeholder.container():

                        st.markdown(
                            "### 🧠 AI Pipeline"
                        )

                        for icon, name in PIPELINE_NODES:

                            status = (
                                st.session_state
                                .pipeline_status[name]
                            )

                            if status == "Completed":

                                st.success(
                                    f"{icon} {name} completed",
                                    icon="✅"
                                )

                            elif status == "Running":

                                st.info(
                                    f"{icon} {name} running...",
                                    icon="🔄"
                                )

                            else:

                                st.caption(
                                    f"{icon} {name} waiting..."
                                )


            # =================================================
            # FINAL BLOG
            # =================================================

            final_blog = final_state.get(
                "final_blog",
                ""
            )

            if not final_blog:

                final_blog = final_state.get(
                    "blog",
                    ""
                )

            st.session_state.generated_blog = final_blog

            progress_bar.progress(
                1.0,
                text="Blog generated successfully!"
            )

            st.success(
                "🎉 Blog generated successfully!",
                icon="✅"
            )

        except Exception as e:

            st.error(
                f"Blog generation failed: {str(e)}",
                icon="❌"
            )


# ============================================================
# GENERATED BLOG
# ============================================================

if st.session_state.generated_blog:

    blog = st.session_state.generated_blog

    word_count = len(
        blog.split()
    )

    reading_time = max(
        1,
        round(word_count / 200)
    )

    completed_agents = sum(
        1
        for status in
        st.session_state.pipeline_status.values()
        if status == "Completed"
    )

    st.markdown(
        "## 📄 Your Generated Blog"
    )

    metric1, metric2, metric3 = st.columns(3)

    with metric1:

        st.metric(
            "WORDS",
            f"{word_count:,}"
        )

    with metric2:

        st.metric(
            "READING TIME",
            f"{reading_time} min"
        )

    with metric3:

        st.metric(
            "AI AGENTS COMPLETED",
            f"{completed_agents}/6"
        )

    st.markdown("")

    # Blog content
    with st.container(border=True):

        st.markdown(blog)

    st.markdown("")

    st.download_button(
        label="⬇️  Download Blog",
        data=blog,
        file_name="blogforge_article.md",
        mime="text/markdown",
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer-text">
        BlogForge AI · Multi-Agent Content Generation
        <br><br>
        Research · Planning · SEO · Writing · Review · Editing
    </div>
    """,
    unsafe_allow_html=True
)