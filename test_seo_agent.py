from agents.research_agent import research_agent
from agents.planner_agent import planner_agent
from agents.seo_agent import seo_agent


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
print("🔍 STEP 3: SEO AGENT")
print("======================================\n")

seo = seo_agent(topic, research, plan)


print("\n======================================")
print("🚀 BLOGFORGE SEO STRATEGY")
print("======================================\n")

print(seo)