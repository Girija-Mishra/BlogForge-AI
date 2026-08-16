import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


# ============================================================
# FAST FREE LLM
# ============================================================

llm = ChatOpenAI(
    model="nvidia/nemotron-nano-9b-v2:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.2,
    timeout=30,
    max_retries=1,
    max_tokens=500
)


# ============================================================
# REVIEWER AGENT
# ============================================================

def reviewer_agent(topic, blog):

    print("🧐 Reviewer Agent started...")
    print("🔍 Checking blog quality...")


    prompt = f"""
You are the Reviewer Agent in BlogForge AI.

Review the following blog quickly and objectively.

BLOG TOPIC:
{topic}

BLOG:
{blog}

Evaluate:

1. Accuracy
2. Structure
3. Readability
4. Grammar
5. SEO
6. Relevance
7. Repetition

Give each a score from 1 to 10.

Then calculate an overall score.

IMPORTANT:
- Do NOT rewrite the blog.
- Keep feedback concise.
- Give only the most important improvements.
- If the blog is good enough, choose PASS.

Return EXACTLY this format:

SCORES:
Accuracy: X/10
Structure: X/10
Readability: X/10
Grammar: X/10
SEO: X/10
Relevance: X/10
Repetition: X/10

OVERALL SCORE: X/10

FINAL DECISION: PASS or REVISE

FEEDBACK:
- Improvement 1
- Improvement 2
- Improvement 3
"""


    response = llm.invoke(prompt)


    print("✅ Review completed!")


    return response.content