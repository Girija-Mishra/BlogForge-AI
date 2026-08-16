import os

from dotenv import load_dotenv
from openai import OpenAI


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# OPENROUTER CLIENT
# ============================================================

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# ============================================================
# IMAGE PROMPT AGENT
# ============================================================

def image_agent(topic: str, blog: str) -> str:

    print("\n🖼️ IMAGE AGENT")
    print("Creating image prompt...")


    prompt = f"""
You are the Image Prompt Agent for BlogForge AI.

Your job is to create ONE detailed prompt for an AI image
generation model.

BLOG TOPIC:
{topic}

BLOG CONTENT:
{blog}

Create a professional hero-image prompt that represents
the main idea of the blog.

Requirements:

- Directly related to the topic
- Professional and visually appealing
- Suitable for a blog website
- Modern editorial / realistic visual style
- Strong composition
- No text
- No letters
- No logos
- No watermarks
- Do not include explanations
- Return ONLY the image-generation prompt

IMAGE PROMPT:
"""


    # ========================================================
    # CALL OPENROUTER
    # ========================================================

    response = client.chat.completions.create(
        model="nvidia/nemotron-nano-9b-v2:free",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        max_tokens=250
    )


    # ========================================================
    # EXTRACT RESPONSE SAFELY
    # ========================================================

    image_prompt = response.choices[0].message.content


    if image_prompt:

        image_prompt = image_prompt.strip()


    # ========================================================
    # FALLBACK
    # ========================================================

    if not image_prompt:

        image_prompt = (
            "A professional modern editorial illustration "
            "showing artificial intelligence transforming "
            "education, with students learning alongside "
            "advanced AI technology in a futuristic but "
            "realistic classroom environment, natural "
            "lighting, cinematic composition, highly "
            "detailed, clean background, no text, no logos, "
            "no watermark, suitable as a professional blog "
            "hero image."
        )


    print("🖼️ Image prompt created.")

    return image_prompt