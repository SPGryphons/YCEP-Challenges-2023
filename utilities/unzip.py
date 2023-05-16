import os
import zipfile

# zip files should be in the same directory as this script

def unzip_file(zip_src, dst_dir):
    try:
        with zipfile.ZipFile(zip_src) as z:
            z.extractall(path=dst_dir)
    except Exception as e:
        print("[*] Uh oh, something went wrong!")
        print(e + "\n" + zip_src)

if __name__ == '__main__':
    files = os.listdir()
    for file in files:
        if file.endswith('.zip'):
            unzip_file(file, os.path.splitext(file)[0])