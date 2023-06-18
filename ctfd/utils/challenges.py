import requests
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

class ChallengeHandler:
    def __init__(self, session: requests.Session, URL: str):
        self.session = session
        self.URL = URL

    def get_challenges(self) -> Dict[str, List[Dict[str, str]]]:
        response = self.session.get(f"{self.URL}/challenges").json()
        return response

    def post_challenge(self, challenge: Dict[str, str]) -> Tuple[bool, List[str]]:
        response: dict = self.session.post(
            f"{self.URL}/challenges", json=challenge).json()

        success = response.get("success", False)
        errors = response.get("errors", [])

        return success, errors
