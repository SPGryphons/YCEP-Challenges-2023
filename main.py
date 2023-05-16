import argparse
from utils.collate import Counter
from utils.unzip import ZipHandler

parser = argparse.ArgumentParser()
parser.add_argument("-X", "--unzip-all", help="Unzip all files in directory", action="store_true")
parser.add_argument("-c", "--count", help="Count number of challenges", action="store_true")
parser.add_argument("-cA", "--diffs", help="Count number of challenges by difficulty and total", action="store_true")

args = parser.parse_args()

if __name__ == '__main__':
    if args.unzip_all:
        zip_handler = ZipHandler()
        zip_handler.unzip_all()

    elif args.count:
        counter = Counter(
            categories=["crypto", "forensics", "misc","osint", "pwn", "reverse", "web"],
            path="./challenges/"
        )
        counter.count()
    elif args.diffs:
        counter = Counter(
            categories=["crypto", "forensics", "misc","osint", "pwn", "reverse", "web"],
            path="./challenges/"
        )
        counter.count_diffs()
    
    else:
        print("No arguments passed. Use -h or --help for help.")