import os   
import string
import random
import csv
import logging
from typing import Dict, List
from utils.env import fetch_env
from utils.users import UserHandler 

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

def generate_password():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def create_users(users: List[Dict[str, str]]) -> None:
    logging.info("Creating users...")
    count = 0
    errors = []
    for user in users:
        if(user["password"]):
            logging.debug(f"Skipping {user['username']}...")
            continue
        user["password"] = generate_password()
        user_object = {
            "name": user["username"],
            "email": user["email"],
            "password": user["password"],
            "type": "user",
            "verified": "true",
            "banned": "false",
            "hidden": "false"
        }

        success, error = User.create_user(user_object)
        if success:
            logging.info(f"Created {user['username']}.")
            count += 1
        else:
            errors.append(error)
            user["password"] = ""
            logging.error(f"Failed to create {user['username']} with error: {errors[-1]}")
    logging.info(f"Task completed with {count} users created and {len(errors)} errors.")
    if(not errors):
        write_csv("./csv/users.csv", users)

if __name__ == "__main__":
    log_setup()
    API_KEY = fetch_env()
    URL = os.getenv("URL") # temp
    User = UserHandler(API_KEY, URL)

    user_list = load_csv("./csv/users.csv")
    create_users(user_list)