import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_image_url(query: str):
    """
    Search Pexels for a relevant photo.
    Returns:
        image_url, photographer_name, photographer_url
    """

    api_key = os.getenv("PEXELS_API_KEY")

    if not api_key:
        raise ValueError(
            "PEXELS_API_KEY is missing from .env"
        )

    query = query.strip()

    if not query:
        query = "technology education"

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": api_key
    }

    params = {
        "query": query,
        "per_page": 10,
        "orientation": "landscape"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    photos = data.get("photos", [])

    if not photos:
        raise RuntimeError(
            f"No Pexels images found for: {query}"
        )

    # Pick the first relevant landscape image
    photo = photos[0]

    image_url = photo["src"]["large2x"]

    photographer = photo.get(
        "photographer",
        "Pexels photographer"
    )

    photographer_url = photo.get(
        "photographer_url",
        "https://www.pexels.com/"
    )

    print("✅ Pexels image found!")
    print(f"📸 Photographer: {photographer}")

    return (
        image_url,
        photographer,
        photographer_url
    )