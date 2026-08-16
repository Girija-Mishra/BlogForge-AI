from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.research_agent import research_agent
from agents.planner_agent import planner_agent
from agents.seo_agent import seo_agent
from agents.writer_agent import writer_agent
from agents.reviewer_agent import reviewer_agent
from agents.editor_agent import editor_agent


# ============================================================
# SHARED STATE
# ============================================================

class BlogState(TypedDict, total=False):

    topic: str

    audience: str
    tone: str
    length: str

    research: str
    plan: str
    seo: str
    blog: str
    review: str
    final_blog: str


# ============================================================
# RESEARCH NODE
# ============================================================

def research_node(state: BlogState):

    print("\n🔎 RESEARCH AGENT")

    research = research_agent(
        state["topic"]
    )

    return {
        "research": research
    }


# ============================================================
# PLANNER NODE
# ============================================================

def planner_node(state: BlogState):

    print("\n📋 CONTENT PLANNER")

    plan = planner_agent(
        state["topic"],
        state["research"]
    )

    return {
        "plan": plan
    }


# ============================================================
# SEO NODE
# ============================================================

def seo_node(state: BlogState):

    print("\n🔍 SEO AGENT")

    seo = seo_agent(
        state["topic"],
        state["research"],
        state["plan"]
    )

    return {
        "seo": seo
    }


# ============================================================
# WRITER NODE
# ============================================================

def writer_node(state: BlogState):

    print("\n✍️ WRITER AGENT")

    blog = writer_agent(
        state["topic"],
        state["research"],
        state["plan"],
        state["seo"],
        state.get(
            "audience",
            "General readers"
        ),
        state.get(
            "tone",
            "Professional"
        ),
        state.get(
            "length",
            "Medium"
        )
    )

    return {
        "blog": blog
    }


# ============================================================
# REVIEWER NODE
# ============================================================

def reviewer_node(state: BlogState):

    print("\n🧐 REVIEWER AGENT")

    review = reviewer_agent(
        state["topic"],
        state["blog"]
    )

    return {
        "review": review
    }


# ============================================================
# EDITOR NODE
# ============================================================

def editor_node(state: BlogState):

    print("\n🛠️ EDITOR AGENT")

    final_blog = editor_agent(
        state["topic"],
        state["blog"],
        state["review"]
    )

    return {
        "final_blog": final_blog
    }


# ============================================================
# REVIEW DECISION
# ============================================================

def review_decision(state: BlogState):

    review = state["review"].upper()


    if "FINAL DECISION: PASS" in review:

        print("\n✅ REVIEW PASSED")

        return "pass"


    print("\n🔄 REVIEW REQUIRES REVISION")

    return "edit"


# ============================================================
# FINALIZER
# ============================================================

def finalizer_node(state: BlogState):

    print("\n🏁 FINALIZING BLOG...")


    # If Editor created a revised version
    if state.get("final_blog"):

        return {
            "final_blog": state["final_blog"]
        }


    # Otherwise use Writer output
    return {
        "final_blog": state["blog"]
    }


# ============================================================
# BUILD WORKFLOW
# ============================================================

def build_blog_workflow():

    graph = StateGraph(
        BlogState
    )


    # --------------------------------------------------------
    # ADD NODES
    # --------------------------------------------------------

    graph.add_node(
        "research",
        research_node
    )

    graph.add_node(
        "planner",
        planner_node
    )

    graph.add_node(
        "seo",
        seo_node
    )

    graph.add_node(
        "writer",
        writer_node
    )

    graph.add_node(
        "reviewer",
        reviewer_node
    )

    graph.add_node(
        "editor",
        editor_node
    )

    graph.add_node(
        "finalizer",
        finalizer_node
    )


    # --------------------------------------------------------
    # MAIN FLOW
    # --------------------------------------------------------

    graph.add_edge(
        START,
        "research"
    )

    graph.add_edge(
        "research",
        "planner"
    )

    graph.add_edge(
        "planner",
        "seo"
    )

    graph.add_edge(
        "seo",
        "writer"
    )

    graph.add_edge(
        "writer",
        "reviewer"
    )


    # --------------------------------------------------------
    # REVIEW DECISION
    # --------------------------------------------------------

    graph.add_conditional_edges(

        "reviewer",

        review_decision,

        {
            "pass": "finalizer",
            "edit": "editor"
        }
    )


    # --------------------------------------------------------
    # EDITOR → FINALIZER
    # --------------------------------------------------------

    graph.add_edge(
        "editor",
        "finalizer"
    )


    # --------------------------------------------------------
    # FINALIZER → END
    # --------------------------------------------------------

    graph.add_edge(
        "finalizer",
        END
    )


    # --------------------------------------------------------
    # COMPILE
    # --------------------------------------------------------

    return graph.compile()


# ============================================================
# CREATE WORKFLOW
# ============================================================

blog_workflow = build_blog_workflow()