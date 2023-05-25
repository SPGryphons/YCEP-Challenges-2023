import os
from dotenv import load_dotenv

def fetch_env() -> None | str:
    if not os.path.exists(".env"):
        print("No .env file found! Please create one and try again!")
        exit(1)
    else:
        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        if API_KEY is None:
            print("Missing API_KEY in .env file! Please add them and try again!")
            exit(1)
        else:
            return API_KEY