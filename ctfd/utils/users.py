import requests
import random
import string
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


class UserHandler:
    def __init__(self, session: requests.Session, URL: str):
        self.session = session
        self.URL = URL

    def get_users(self) -> Dict[str, List[Dict[str, str]]]:
        response = self.session.get(f"{self.URL}/users").json()
        return response

    def post_user(self, user: Dict[str, str]) -> Tuple[bool, List[str]]:
        response: dict = self.session.post(
            f"{self.URL}/users", json=user).json()

        success = response.get("success", False)
        errors = response.get("errors", [])

        return success, errors

@dataclass
class User:
    username: str
    email: str
    password: Optional[str] = None

    def __post_init__(self):
        self.password = self._generate_password()

    @staticmethod
    def _generate_password() -> str:
        return ''.join(random.choice(string.ascii_letters) for _ in range(10))

    def generate_user(self) -> Dict[str, str]:
        return {
            "name": self.username,
            "email": self.email,
            "password": self.password,
            "type": "user",
            "verified": "true",
            "banned": "false",
            "hidden": "false"
        }
