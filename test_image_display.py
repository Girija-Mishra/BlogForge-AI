from utils.image_utils import get_image_url


print("\n======================================")
print("🖼️ BLOGFORGE PEXELS IMAGE TEST")
print("======================================")

topics = [
    "artificial intelligence education",
    "climate change",
    "cybersecurity"
]

for topic in topics:

    print(f"\n🔎 Searching: {topic}")

    try:

        image_url, photographer, photographer_url = get_image_url(topic)

        print("✅ Image found!")
        print(f"🖼️ URL: {image_url}")
        print(f"📸 Photographer: {photographer}")
        print(f"🔗 Photographer URL: {photographer_url}")

    except Exception as e:

        print("❌ IMAGE SEARCH FAILED")
        print(e)