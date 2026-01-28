import pandas as pd
from datetime import datetime, timedelta
import random


class MockParkingAPI:
    def __init__(self, city: str):
        self.city = city

    def fetch_parking_data(self) -> pd.DataFrame:
        now = datetime.utcnow()
        data = []

        for i in range(20):
            data.append(
                {
                    "timestamp": now - timedelta(minutes=5 * i),
                    "name": "Mock Parking",
                    "available": random.randint(20, 80),
                    "total": 100,
                }
            )

        df = pd.DataFrame(data)
        df = df.sort_values("timestamp")

        return df
