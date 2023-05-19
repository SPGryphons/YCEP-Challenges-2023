import os
import glob
import shutil

# Get all folders in current directory, read the README.md file in each folder
# and find the category it is in, then move the folder to that category folder
# if it is not already in that folder

mapping = {
  "crypto": ["crypto", "cryptography"],
  "forensics": ["forensics", "forensic"],
  "misc": ["misc", "miscellaneous"],
  "pwn": ["pwn", "pwnable"],
  "reverse": ["reversing", "reverse", "reverse engineering", "rev"],
  "web": ["web", "web exploitation", "web_exploitation"],
  "osint": ["osint", "open source intelligence"]
}

ignore_files = ["utils", "challenges", "README.md", "main.py"]

class Sorter:
    def __init__(self, path: str = "./"):
        self.path = path

    def strip_formatting(self, line: str) -> str:
        # remove everything that isnt alphanumeric or a space
        return "".join([c for c in line if c.isalnum() or c == " "])

    def get_category(self, folder: str) -> str:
        if not os.path.exists(folder + "/README.md"):
            return None
        with open(folder + "/README.md", "r") as f:
            for line in f.readlines():
                if "category" in line.lower():
                    category = self.strip_formatting(line.lower().split("category")[1]).strip()
                    for key in mapping:
                        for value in mapping[key]:
                            if value in category:
                                return key
                    return None
        return None

    def sort_all(self):
        for folder in glob.glob("*"):
            if folder not in ignore_files:
                category = self.get_category(folder)
                if category is not None:
                    shutil.move(folder, self.path + category)
                else:
                    print("Unable to find category for", folder)