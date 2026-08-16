from agents.image_agent import image_agent


topic = "Impact of Artificial Intelligence on Education"

blog = """
Artificial Intelligence is transforming education through
personalized learning, intelligent tutoring systems,
automated assessment, and learning analytics.
"""


print("\n======================================")
print("🖼️ BLOGFORGE IMAGE AGENT TEST")
print("======================================")


image_prompt = image_agent(
    topic,
    blog
)


print("\n======================================")
print("IMAGE PROMPT")
print("======================================\n")


print(image_prompt)