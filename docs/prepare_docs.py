import os
import shutil
from pathlib import Path

for f in os.listdir('.'):
    print(f)

def replaceLinksInFiles():
    for root, _, fileNames in os.walk("docs"):
        for fileName in fileNames:
            if fileName.split('.')[-1] != 'md':
                continue

            with open(f"{root}/{fileName}", 'r') as file:
                content = file.read()

            content = content.replace("/.eraser/", "/img/")

            with open(f"{root}/{fileName}", 'w') as file:
                file.write(content)

def moveImagesToImgFolder():
    if not os.path.exists("img"):
        os.mkdir("img")

    for root, _, fileNames in os.walk(".eraser"):
        for fileName in fileNames:
            # shutil.move(f"{root}/{fileName}", f"docs/img/{fileName}")
            file = Path(f"{root}/{fileName}")

            print(file.name)

            file.rename(f"docs/img/{fileName}")

replaceLinksInFiles()
moveImagesToImgFolder()