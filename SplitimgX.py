import cv2
from pathlib import Path
import shutil

def SplitimgX(source_path,landscapes_path,Portraits_path,extentions):
    landscapes_path.mkdir(exist_ok=True)
    Portraits_path.mkdir(exist_ok=True)
    for folder in source_path.iterdir():
        if folder.is_dir():
            SplitimgX(folder,landscapes_path / folder.name,Portraits_path / folder.name,extentions)
        elif folder.is_file():
            if folder.suffix.lower() in extentions :
                img=cv2.imread(f"{folder}")
                print(folder.name)
                print(img.shape[0])
                print(img.shape[1])

                if img.shape[0]<img.shape[1]:
                    shutil.copy(str(folder),str(landscapes_path / folder.name))
                else:
                    shutil.copy(str(folder), str(Portraits_path / folder.name))




p=input("Enter the parent path : ")
path=Path(rf"{p}")
Lpath=path.parent / f"{path.name}Landscape"
Ppath=path.parent / f"{path.name}Portrait"

extentions=input("enter extentions please (.png .jpg)").lower().split(" ")

SplitimgX(path,Lpath,Ppath,extentions)