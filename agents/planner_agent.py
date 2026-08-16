import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


# ============================================================
# FAST LLM
# ============================================================

llm = ChatOpenAI(
    model="nvidia/nemotron-nano-9b-v2:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.3,
    timeout=30,
    max_retries=1,
    max_tokens=500
)


# ============================================================
# CONTENT PLANNER AGENT
# ============================================================

def planner_agent(topic, research):

    print("📋 Content Planner started...")
    print("🤖 Creating concise blog structure...")


    prompt = f"""
You are the Content Planner Agent in BlogForge AI.

Create a concise structure for a blog.

BLOG TOPIC:
{topic}

RESEARCH:
{research}

Return ONLY:

1. Blog title
2. Introduction idea
3. 4-5 main H2 sections
4. Key points for each section
5. One real-world example
6. Conclusion idea
7. Target audience
8. Suggested tone

Rules:
- Use the supplied research.
- Do not write the complete blog.
- Keep the plan concise.
- Do not repeat the research.
"""


    response = llm.invoke(prompt)


    print("✅ Content plan created!")


    return response.content