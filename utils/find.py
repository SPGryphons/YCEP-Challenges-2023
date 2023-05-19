import glob

class Finder:
    def __init__(self, path: str = "./challenges"):
        self.path = path

    def find_challenge(self, challenge: str) -> str:
        # Search in every category in the challenges folder
        for category in glob.glob(self.path + "/*"):
        # Search in every challenge in the category
            for challenge_folder in glob.glob(category + "/*"):
                if challenge.lower() in challenge_folder.lower():
                    print("Found", challenge_folder)
                    print("Category:", category)
                    return
        print("Unable to find challenge", challenge)