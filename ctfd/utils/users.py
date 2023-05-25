import requests
from typing import Dict, List, Tuple

class UserHandler:
    @staticmethod
    def generate_session(API_KEY: str) -> requests.Session:
        r = requests.Session()
        r.headers.update({"Authorization": f"Token {API_KEY}"})
        return r
    
    def __init__(self, API_KEY: str, URL: str):
        self.session: requests.Session = self.generate_session(API_KEY)
        self.URL: str = URL

    def get_users(self) -> Dict[str, List[Dict]]:
        response = self.session.get(self.URL + "/users").json()
        return response

    def create_user(self, user: dict) -> bool | Tuple[bool, List[str]]:
        response = self.session.post(self.URL + "/users", json=user).json()
        if response["success"]:
            return True, []
        else:
            return False, response["error"]