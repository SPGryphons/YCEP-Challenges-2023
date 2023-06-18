import os
import csv
import requests
import logging
from typing import Dict, List
from utils.env import fetch_env
from utils.users import User, UserHandler


def generate_session(API_KEY: str) -> requests.Session:
    session = requests.Session()
    session.headers.update({"Authorization": f"Token {API_KEY}"})
    return session

def log_setup() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("ctfd.log"),
            logging.StreamHandler()
        ]
    )


def load_csv(file: str) -> List[Dict[str, str]]:
    logging.info(f"Loading {file}...")
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def write_csv(file: str, data: List[Dict[str, str]]) -> None:
    logging.info(f"Writing {file}...")
    with open(file, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def find_users() -> str:
    logging.info("Searching for 'users.csv'...")
    root_dir = os.getcwd()
    for r, d, f in os.walk(root_dir):
        if "users.csv" in f:
            relative_path = os.path.relpath(os.path.join(
                r, "users.csv"), start=root_dir).replace(os.sep, '/')
            logging.info(
                f"Found 'users.csv' in {os.path.join(r, 'users.csv')}")
            return f"./{relative_path}"

    return None


def create_users(users: List[Dict[str, str]]) -> None:
    logging.info("Creating users...")

    success_list: List[Dict[str, str]] = []
    error_list: List[Dict[str, str]] = []

    for user in users:
        if user["password"] != "":
            logging.debug(f"Skipping {user['username']}...")
            continue

        user_object: Dict[str, str] = User(
            user["username"],
            user["email"],
            user["password"]).generate_user()

        success, error = UserAPI.post_user(user_object)
        if success == True:
            logging.info(f"Created {user['username']}.")
            user["password"] = user_object["password"]
            success_list.append(user)
        else:
            error_list.append(user)
            logging.error(
                f"Failed to create '{user['username']}' with error: {error}")

    logging.info(
        f"Task completed with {len(success_list)} users created and {len(error_list)} errors.")
    if not error_list:
        write_csv("./csv/users.csv", users)


if __name__ == "__main__":

    log_setup()
    API_KEY: str = fetch_env()
    SESSION: requests.Session = generate_session(API_KEY)
    URL: str = os.getenv("URL")

    if URL:
        logging.info(f"Using URL: {URL}")
    else:
        logging.error("No URL found in environment variables.")
        exit(1)

    UserAPI: UserHandler = UserHandler(SESSION, URL)

    user_list = find_users()
    if user_list == None:
        logging.error("'users.csv' could not be found.t")
        exit(1)
    else:
        user_list: List[Dict[str, str]] = load_csv(user_list)
        create_users(user_list)

    logging.info("All tasks completed, peacefully exiting...")
