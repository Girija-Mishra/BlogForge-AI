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
    max_tokens=700
)


# ============================================================
# RESEARCH AGENT
# ============================================================

def research_agent(topic):

    print("🔎 Research Agent started...")
    print(f"📚 Topic: {topic}")
    print("🤖 Researching with fast Nemotron...")


    prompt = f"""
You are the Research Agent in BlogForge AI.

Research this topic:

{topic}

Give concise information for a blog writer.

Return ONLY:

1. Brief overview
2. 5 important points
3. 3 important facts or concepts
4. 2 real-world examples
5. 3 benefits
6. 3 challenges
7. 8 useful keywords

Do NOT write the final blog.

Keep the response concise and factual.
"""


    response = llm.invoke(prompt)


    print("✅ Research completed!")


    return response.content
