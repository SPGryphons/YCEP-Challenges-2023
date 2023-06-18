import glob

class Finder:
    def __init__(self, path: str = "./challenges"):
        self.path = path

    def _find_challenge(self, challenge: str) -> list:
        # Search in every category in the challenges folder
        found = []
        for category in glob.glob(self.path + "/*"):
        # Search in every challenge in the category
            for challenge_folder in glob.glob(category + "/*"):
                if challenge.lower() in challenge_folder.lower():
                    found.append((challenge_folder, category))
        return found

    def find_challenge(self, challenge: str) -> str:
        found = self._find_challenge(challenge)
        if len(found) == 0:
            print("Unable to find challenge", challenge)
        else:
            print("Found", len(found), "matches for", challenge)
            for i, (challenge_folder, category) in enumerate(found):
                print(i+1, challenge_folder, "in", category)