import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


# ============================================================
# FAST LLM
# ============================================================

llm = ChatOpenAI(
    model="openrouter/free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.3,
    timeout=30,
    max_retries=1,
    max_tokens=450
)


# ============================================================
# SEO AGENT
# ============================================================

def seo_agent(topic, research, plan):

    print("🔍 SEO Agent started...")
    print("🤖 Creating SEO strategy...")


    prompt = f"""
You are the SEO Agent in BlogForge AI.

Create a concise SEO strategy for this blog.

BLOG TOPIC:
{topic}

RESEARCH:
{research}

BLOG PLAN:
{plan}

Return ONLY:

1. Primary keyword
2. 5 secondary keywords
3. 3 long-tail keywords
4. SEO-friendly title
5. Meta description under 160 characters
6. URL slug
7. Search intent
8. 3 relevant FAQ questions

Rules:
- Keep keywords natural.
- Avoid keyword stuffing.
- Do not write the blog.
- Keep the response concise.
"""


    response = llm.invoke(prompt)


    print("✅ SEO strategy created!")


    return response.content
