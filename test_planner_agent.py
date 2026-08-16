from agents.research_agent import research_agent
from agents.planner_agent import planner_agent


topic = "Impact of Artificial Intelligence on Education"

print("\n======================================")
print("🔎 STEP 1: RESEARCH AGENT")
print("======================================\n")

research = research_agent(topic)

print("\n======================================")
print("📋 STEP 2: CONTENT PLANNER")
print("======================================\n")

plan = planner_agent(topic, research)

print("\n======================================")
print("📝 BLOG PLAN")
print("======================================\n")

print(plan)