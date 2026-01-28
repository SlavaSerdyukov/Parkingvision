import os
import requests

from parkingvision.app.api.base import ParkingAPI


class HereParkingAPI(ParkingAPI):
    def __init__(self, city, lat, lon, radius=5000):
        self.city = city
        self.lat = lat
        self.lon = lon
        self.radius = radius
        self.api_key = os.getenv("HERE_API_KEY")

    def fetch(self) -> list[dict]:
        if not self.api_key:
            return []

        url = "https://discover.search.hereapi.com/v1/discover"
        params = {
            "q": "parking",
            "at": f"{self.lat},{self.lon}",
            "limit": 20,
            "apiKey": self.api_key,
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
        except Exception:
            return []

        result = []
        for item in data.get("items", []):
            result.append(
                {
                    "name": item.get("title", "Unknown"),
                    "available": None,
                    "total": None,
                }
            )

        return result
