import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


# ============================================================
# EDITOR LLM
# ============================================================

llm = ChatOpenAI(
    model="nvidia/nemotron-nano-9b-v2:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.3,
    timeout=60,
    max_retries=1,
    max_tokens=4000
)


# ============================================================
# EDITOR AGENT
# ============================================================

def editor_agent(topic, blog, review):

    print("\n🛠️ Editor Agent started...")
    print("✏️ Improving the blog based on reviewer feedback...")


    prompt = f"""
You are the Editor Agent in BlogForge AI.

Your job is to produce the FINAL polished version of the
blog while preserving the useful content written by the
Writer Agent.

IMPORTANT:
The original blog may already be long and detailed.

DO NOT unnecessarily shorten the article.

DO NOT summarize the original blog.

DO NOT replace detailed sections with short paragraphs.

DO NOT remove useful examples, explanations, applications,
facts, headings, or important details merely to make the
article shorter.


============================================================
BLOG TOPIC
============================================================

{topic}


============================================================
ORIGINAL BLOG
============================================================

{blog}


============================================================
REVIEWER FEEDBACK
============================================================

{review}


============================================================
EDITING INSTRUCTIONS
============================================================

1. Correct the important issues identified by the reviewer.

2. Improve grammar, clarity and readability.

3. Improve the structure only when necessary.

4. Preserve the original article's useful content.

5. Preserve detailed explanations.

6. Preserve useful examples.

7. Preserve real-world applications.

8. Preserve important facts from the original article.

9. Preserve the major sections and headings unless
   the reviewer specifically identifies a structural problem.

10. Naturally maintain relevant SEO keywords.

11. Use proper Markdown formatting.

12. Use H2 headings for major sections.

13. Use H3 headings where useful.

14. Keep the introduction engaging.

15. Keep the conclusion meaningful.

16. Do not mention the reviewer, editor, AI agents,
    workflow, or BlogForge inside the article.

17. Do not invent statistics, facts or sources.

18. Do not add meaningless filler just to increase length.

19. MOST IMPORTANT:
    Preserve the approximate length of the original blog.

20. If the original blog is already detailed, keep it detailed.

21. Only remove content when it is repetitive, incorrect,
    irrelevant, or specifically criticized by the reviewer.

22. Return ONLY the final blog article.

============================================================
FINAL ARTICLE
============================================================
"""


    response = llm.invoke(prompt)

    final_blog = response.content.strip()

    print("✅ Final blog created!")
    print(f"📏 Final blog characters: {len(final_blog)}")
    print(f"📝 Final blog words: {len(final_blog.split())}")

    return final_blog