import os

DIFFICULTIES = ["easy", "medium", "hard", "extreme"]

mapping = {
  "crypto": ["crypto", "cryptography"],
  "forensics": ["forensics", "forensic"],
  "misc": ["misc", "miscellaneous"],
  "pwn": ["pwn", "pwnable"],
  "reverse": ["reversing", "reverse", "reverse engineering", "rev"],
  "web": ["web", "web exploitation", "web_exploitation"],
  "osint": ["osint", "open source intelligence"]
}

class Counter:
    def __init__(self, categories: list[str], path: str):
        self.categories = categories
        self.path = path

    def _count(self) -> dict[str, int]:
        collated = {}
        for category in self.categories:
            files = os.listdir(self.path + category)
            collated[category] = len(files)
        # Sort the catergories by the number of challenges in each
        return {
            k: v 
            for k, v in sorted(
                collated.items(),
                key=lambda item: item[1],
                reverse=True
            )
        }
    
    def strip_formatting(self, line: str) -> str:
        """Remove everything that isnt alphanumeric or a space"""
        return "".join([c for c in line if c.isalnum() or c == " "])
    

    def get_difficulty(self, folder: str) -> str | None:
        """Find the difficulty of a challenge from its README.md file"""
        if not os.path.exists(folder + "/README.md"):
            print(f"Unable to find README.md for {folder}")
            return None
        with open(folder + "/README.md", "r", encoding="utf-8") as f:
            for line in f.readlines():
                if "difficulty:" in line.lower():
                    difficulty = self.strip_formatting(
                        line.lower().split("difficulty")[1].strip()
                    ).strip()
                    print(difficulty)
                    if difficulty.lower() in DIFFICULTIES:
                        return difficulty
                    else:
                        print(difficulty)
        return None
        
    def get_chall_infos(self) -> dict[str, list[str, str | None]]:
        """Gets the difficulty and category of each challenge"""
        infos = {}
        for category in self.categories:
            files = os.listdir(self.path + category)
            for file in files:
                diff = self.get_difficulty(
                    self.path + category + "/" + file
                )
                infos[file] = [category, diff]
        return infos
    
    def _count_diffs(self) -> dict[str, dict[str, int]]:
        """Counts the number of challenges in each difficulty"""
        infos = self.get_chall_infos()
        difficulties = {
            category: {
                diff: 0 for diff in DIFFICULTIES
            } for category in self.categories
        }
        for chall, info in infos.items():
            category, diff = info
            if diff is None:
                print(f"Unable to find difficulty for {chall}")
                continue
            difficulties[category][diff] += 1
        return difficulties
    

    def count(self):
        """Counts the number of challenges in each category"""
        collated = self._count()
        for category, count in collated.items():
            print(f"{category.capitalize()}: {count}")
        print(f"Total: {sum(collated.values())}")

    def count_diffs(self):
        """Counts the number of challenges in each difficulty"""
        difficulties = self._count_diffs()
        total_diffs = {diff: 0 for diff in DIFFICULTIES}
        for category, diffs in difficulties.items():
            print(category.capitalize())
            for diff, count in diffs.items():
                total_diffs[diff] += count
                print(f"\t{diff.capitalize()}: {count}")
            print("-------------------")
        print(f"Total: {sum(total_diffs.values())}")
        for diff, count in total_diffs.items():
            print(f"\t{diff.capitalize()}: {count}")



if __name__ == '__main__':
    counter = Counter(
        categories=["crypto", "forensics", "misc",
                    "osint", "pwn", "reverse", "web"],
        path="../challenges/"
    )
    counter.count_diffs()
    counter.count()
