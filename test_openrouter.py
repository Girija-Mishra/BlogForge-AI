import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7
)

response = llm.invoke(
    "Explain what a multi-agent AI system is in 3 simple sentences."
)

print("\n🤖 Nemotron 3 Super Response:\n")
print(response.content)