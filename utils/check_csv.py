from utils.find import Finder

def check_csv(file: str):
    finder = Finder()

    matcher = []

    with open(file, "r") as f:
        for line in f.readlines():
            if line.startswith("Timestamp"):
                continue
            if len(line) < 3:
                continue
            line = line.strip()
            if len(line) == 0:
                continue
            line = line.split(",")
            found = finder._find_challenge(line[3])
            if len(found) == 0:
                found = finder._find_challenge(line[7].rsplit(".", 1)[0])
                if len(found) == 0:
                    print("Unable to find challenge", line[3], "or", line[7].rsplit(".", 1)[0])
                    continue
            elif len(found) > 1:
                print("Found multiple challenges for", line[3], "or", line[7].rsplit(".", 1)[0], ":", found)

            if found not in matcher:
                matcher.append(found)
            else:
                print("Found duplicate challenge", found, "for", line[3], "or", line[7].rsplit(".", 1)[0])
                continue

            print("Found challenge", found, "for", line[3], "or", line[7].rsplit(".", 1)[0])