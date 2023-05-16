import os
class Counter:
    def __init__(self, categories: list[str], path: str):
        self.categories = categories
        self.path = path

    def collate(self) -> dict[str, int]:
        collated = {}
        for category in self.categories:
            files = os.listdir(self.path + category)
            collated[category] = len(files)
        return {k: v for k, v in sorted(collated.items(), key=lambda item: item[1], reverse=True)}
    
    def print_count(self):
        collated = self.collate()
        for category, count in collated.items():
            print(f"{category}: {count}")
        print(f"Total: {sum(collated.values())}")

if __name__ == '__main__':
    counter = Counter(
        categories=["crypto", "forensics", "misc", "osint", "pwn", "reverse", "web"], 
        path="../challenges/"
    )
<<<<<<< HEAD
    counter.print_count()
=======
    # counter.print_count()
>>>>>>> 74357d417835e41c1a49ecdc74c46de68f433ea2
