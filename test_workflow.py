from workflow.blog_workflow import blog_workflow


print("\n======================================")
print("🚀 BLOGFORGE COMPLETE WORKFLOW TEST")
print("======================================")


topic = "Impact of Artificial Intelligence on Education"


print(f"\n📝 Topic: {topic}")
print("\nStarting BlogForge...\n")


result = blog_workflow.invoke({
    "topic": topic
})


print("\n======================================")
print("🎉 BLOGFORGE WORKFLOW COMPLETED")
print("======================================")


# ------------------------------------------------------------
# FINAL BLOG
# ------------------------------------------------------------

final_blog = result.get("final_blog", "")

print("\n📝 FINAL BLOG")
print("--------------------------------------")

print(final_blog[:2000])

print("\n... (blog output truncated for terminal)")


# ------------------------------------------------------------
# IMAGE
# ------------------------------------------------------------

image_url = result.get("image_url", "")

print("\n🖼️ IMAGE URL")
print("--------------------------------------")

print(image_url)


# ------------------------------------------------------------
# FINAL STATUS
# ------------------------------------------------------------

print("\n======================================")
print("✅ TEST COMPLETE")
print("======================================")

if final_blog:
    print("✅ Final blog received")
else:
    print("❌ Final blog missing")


if image_url:
    print("✅ Image URL received")
else:
    print("❌ Image URL missing")