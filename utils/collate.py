import os
class Counter:
    def __init__(self, categories: list[str], path: str):
        self.categories = categories
        self.path = path

    def __collate__(self) -> dict[str, int]:
        collated = {}
        for category in self.categories:
            files = os.listdir(self.path + category)
            collated[category] = len(files)
        return {k: v for k, v in sorted(collated.items(), key=lambda item: item[1], reverse=True)}

    def __diffs__(self) -> dict[str, list[str]]:
        diffs = {}
        for category in self.categories:
            files = os.listdir(self.path + category)
            for file in files:
                with open(f"{self.path}{category}/{file}/README.md", "r", encoding="utf-8") as f:
                    for line in f:
                        if "Difficulty" in line:
                            diff = line.replace("#", "").replace(
                                "*", "").replace("Difficulty", "").replace(":", "").replace("+", "").replace("-", "").strip()
                            # TODO: fix this stupid hack
                            diffs[file] = [category, diff]
        return diffs

    def __diff_count__(self, category: str, diff: str) -> dict[str, list[str]]:
        diffs = self.__diffs__()
        files = []
        count = 0
        for file, info in diffs.items():
            if info[0] == category and info[1] == diff:
                files.append(file)
                count += 1
        return {
            "count": count,
            "files": files
        }

    def count(self) -> None:
        collated = self.__collate__()
        for category, count in collated.items():
            print(f"{category}: {count}")
        print(f"Total: {sum(collated.values())}")

    def count_diffs(self) -> None:
        count = 0
        diffs = ["Easy", "Medium", "Hard", "Extreme"]
        for category in self.categories:
            for diff in diffs:
                count += self.__diff_count__(category, diff)["count"]
                v = self.__diff_count__(category, diff)
                print(f"{category.title()} [{diff}]: {v['count']}")
            print("-------------------")
        print(f"Total: {count}")
        print("-------------------")


if __name__ == '__main__':
    counter = Counter(
        categories=["crypto", "forensics", "misc",
                    "osint", "pwn", "reverse", "web"],
        path="../challenges/"
    )
    counter.count_diffs()
    counter.count()
