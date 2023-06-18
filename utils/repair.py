import glob
import os
import re
import shutil


class Repair:

    def is_valid_readme(self, file):
        """Checks if the given file is potentially a valid readme file
        This function checks if it specifies a difficulty and a category
        as well has having a flag in the format YCEP2023{...}

        If all checks pass, it returns True, otherwise False
        """
        try:
            file = open(file, "r", encoding="utf-8").read()
        except Exception:
            return False
        if "difficulty" not in file.lower():
            return False
        if "category" not in file.lower():
            return False

        pattern = r'YCEP2023\{[^\}]+\}'
        if not re.search(pattern, file):
            return False

        return True


    def find_readme(self, folder):
        """Tries to find the README.md file in the given folder"""
        files = glob.glob(folder + "/*")
        
        # We first try to find files named readme
        for file in files:
            if "readme" in file.lower():
                if self.is_valid_readme(file):
                    return file
        # If we can't find it, we search more aggressively
        # Check if the file is a markdown file or txt file
        for file in files:
            if file.endswith(".md") or file.endswith(".txt"):
                if self.is_valid_readme(file):
                    return file
        return None
    
    def repair(self, folder):
        """Tries to repair the given folder"""
        # First we check if folder is embedded in another folder
        # If it is, we move the contents of the folder to the parent folder
        # and delete the folder
        # Keep doing this until the length of the files in the folder is more than 1
        at_base = False
        while not at_base:
            files = glob.glob(folder + "/*")
            if len(files) == 1:
                print("Moving embedded folder to parent folder")
                files = folder + "/" + files[0]
                shutil.move(files, folder)
                os.rmdir(files)
            else:
                at_base = True

        # Now we try to find the readme file
        readme = self.find_readme(folder)
        if readme is None:
            print("Unable to auto repair", folder, "please manually repair it")
            return
        print("Found readme in", folder)
        print("Renaming to README.md")
        os.rename(readme, folder + "/README.md")
        print("Done!")