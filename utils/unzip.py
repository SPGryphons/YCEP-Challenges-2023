import os
import glob
import shutil
import zipfile

class ZipHandler:
    def __init__(self, path: str = "./"):
        self.path = path
    
    def unzip_all(self) -> None:
        for file in glob.glob(self.path + "*.zip"):
            with zipfile.ZipFile(file, "r") as zip_ref:
                print("Extracting", file)
                zip_ref.extractall(self.path + file[:-4])
            # check if folder has only one folder in it
            # if so, move all files from that folder to the parent folder
            # and delete the now empty folder
            folder = os.listdir(self.path + file[:-4])
            if len(folder) == 1:
                print("Moving embedded folder to parent folder")
                for f in os.listdir(self.path + file[:-4] + "/" + folder[0]):
                    shutil.move(self.path + file[:-4] + "/" + folder[0] + "/" + f, self.path + file[:-4])
                os.rmdir(self.path + file[:-4] + "/" + folder[0])
            # delete the zip file
            os.remove(file)
    
    def unzip(self, file: str):
        with zipfile.ZipFile(file, "r") as zip_ref:
            zip_ref.extractall(self.path + file[:-4])
            folder = os.listdir(self.path + file[:-4])
            if len(folder) == 1:
                for f in os.listdir(self.path + file[:-4] + "/" + folder[0]):
                    shutil.move(self.path + file[:-4] + "/" + folder[0] + "/" + f, self.path + file[:-4])
                os.rmdir(self.path + file[:-4] + "/" + folder[0])
            # delete the zip file
            os.remove(file)

if __name__ == '__main__':
    zip_handler = ZipHandler()
    zip_handler.unzip()