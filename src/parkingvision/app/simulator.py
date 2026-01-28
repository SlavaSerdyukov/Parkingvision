from datetime import datetime, timedelta
import random
from typing import List, Dict


def generate_synthetic_history(
    parking_name: str,
    hours: int = 6,
    interval_minutes: int = 10,
) -> List[Dict]:
    """
    Generate synthetic parking history data.
    """

    now = datetime.utcnow()
    data = []

    steps = int(hours * 60 / interval_minutes)

    available = random.randint(30, 70)
    total = 100

    for i in range(steps):
        timestamp = now - timedelta(minutes=i * interval_minutes)
        available = max(0, min(total, available + random.randint(-5, 5)))

        data.append(
            {
                "timestamp": timestamp.isoformat(),
                "name": parking_name,
                "available": available,
                "total": total,
            }
        )

    return list(reversed(data))
