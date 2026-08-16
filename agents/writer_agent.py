import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


# ============================================================
# LLM
# ============================================================

llm = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
    timeout=60,
    max_retries=1
)


# ============================================================
# WRITER AGENT
# ============================================================

def writer_agent(
    topic,
    research,
    plan,
    seo,
    audience="General readers",
    tone="Professional",
    length="Medium"
):

    print("\n✍️ Writer Agent started...")
    print("📝 Writing the blog...")
    print(f"👥 Audience: {audience}")
    print(f"🎨 Tone: {tone}")
    print(f"📏 Length: {length}")


    # ========================================================
    # LENGTH INSTRUCTIONS
    # ========================================================

    if length == "Short":

        length_instruction = """
Target approximately 700-900 words.

Keep the article concise but complete.
Cover all important sections from the content plan.
Avoid unnecessary expansion.
"""

    elif length == "Medium":

        length_instruction = """
Target approximately 1200-1600 words.

Develop all major sections properly.
Include explanations, examples, benefits,
challenges and a meaningful conclusion.
"""

    else:

        length_instruction = """
Target approximately 2200-3000 words.

This MUST be a detailed long-form article.

Do not write a short summary.

Expand the major sections from the content plan.

Include:

- Detailed introduction
- Thorough explanations
- H2 headings
- H3 headings where useful
- Multiple relevant examples
- Real-world applications
- Important facts from the research
- Benefits
- Challenges and limitations
- Practical implications
- Detailed conclusion
- FAQ section when appropriate

Do not artificially add meaningless filler.

Do not finish the article early simply because
the basic concepts have been explained.

The final article should genuinely feel like
a professional long-form blog.
"""


    # ========================================================
    # PROMPT
    # ========================================================

    prompt = f"""
You are the Writer Agent in BlogForge AI.

Your task is to write a high-quality, original blog article
using the research, content plan and SEO strategy provided
by the other agents.


============================================================
BLOG TOPIC
============================================================

{topic}


============================================================
TARGET AUDIENCE
============================================================

{audience}


============================================================
WRITING TONE
============================================================

{tone}


============================================================
ARTICLE LENGTH
============================================================

{length}

{length_instruction}


============================================================
RESEARCH
============================================================

{research}


============================================================
CONTENT PLAN
============================================================

{plan}


============================================================
SEO STRATEGY
============================================================

{seo}


============================================================
WRITING REQUIREMENTS
============================================================

1. Write an engaging introduction.

2. Follow the content plan logically.

3. Use clear H2 and H3 Markdown headings.

4. Naturally incorporate the SEO keywords.

5. Explain concepts clearly.

6. Include useful examples.

7. Include relevant real-world applications.

8. Include benefits and challenges.

9. Maintain the requested writing tone.

10. Write specifically for the requested target audience.

11. Avoid unnecessary repetition.

12. Make every major section sufficiently detailed.

13. Write a meaningful conclusion.

14. If the selected length is LONG, produce a genuinely
    detailed long-form article.

15. Do not mention AI agents in the final article.

16. Do not invent statistics or sources.

17. Use Markdown formatting.

18. Return ONLY the final blog article.


============================================================
FINAL LENGTH REQUIREMENT
============================================================

The user selected:

{length}

Follow the requested length carefully.

Do not summarize multiple major sections into one
short paragraph.

For LONG articles especially, develop each section
with explanation, examples and practical context.

Write the final blog article now.
"""


    # ========================================================
    # CALL MODEL
    # ========================================================

    response = llm.invoke(prompt)


    print("✅ Blog draft created!")

    return response.content