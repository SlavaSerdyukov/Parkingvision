from abc import ABC, abstractmethod
from typing import List, Dict


class BaseParkingAPI(ABC):
    """
    Base interface for all parking API adapters.
    """

    @abstractmethod
    def fetch_parking_data(self) -> List[Dict]:
        """
        Must return a list of dicts with:
        {
            "timestamp": str (ISO),
            "name": str,
            "available": int,
            "total": int
        }
        """
        pass
