#!/usr/bin/python3

import argparse
from utils.collate import Counter
from utils.unzip import ZipHandler
from utils.sorter import Sorter
from utils.find import Finder
from utils.repair import Repair
from utils.check_csv import check_csv

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sort", help="Sort all challenges into their respective categories", action="store_true")
parser.add_argument("-X", "--unzip-all", help="Unzip all files in directory", action="store_true")
parser.add_argument("-c", "--count", help="Count number of challenges", action="store_true")
parser.add_argument("-cA", "--diffs", help="Count number of challenges by difficulty and total", action="store_true")
parser.add_argument("-f", "--find", help="Find a challenge")
parser.add_argument("-r", "--repair", help="Attempt to repair a challenge, may not work all the time")
parser.add_argument("-C", "--check-csv", help="Check a csv file for challenges")

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
        
    elif args.sort:
        sorter = Sorter(path="./challenges/")
        sorter.sort_all()

    elif args.find:
        finder = Finder()
        finder.find_challenge(args.find)

    elif args.repair:
        repair = Repair()
        try:
            repair.repair(args.repair)
        except Exception as e:
            print(e.args)
            print("Unable to repair challenge.")
    
    elif args.check_csv:
        check_csv(args.check_csv)
    
    else:
        print("No arguments passed. Use -h or --help for help.")