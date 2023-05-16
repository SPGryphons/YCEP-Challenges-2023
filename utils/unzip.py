import os
import zipfile

class ZipHandler:
    def __init__(self, path: str = "./"):
        self.path = path
    
    def unzip_all(self) -> None:
        for file in os.listdir(self.path):
            if file.endswith(".zip"):
                with zipfile.ZipFile(file, "r") as zip_ref:
                    zip_ref.extractall(self.path)
    
    def unzip(self, file: str):
        with zipfile.ZipFile(file, "r") as zip_ref:
            zip_ref.extractall(self.path)

if __name__ == '__main__':
    zip_handler = ZipHandler()
    zip_handler.unzip()