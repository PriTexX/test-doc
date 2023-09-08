import os

def replaceLinksInFiles():
    for root, _, fileNames in os.walk("./docs"):
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

    for fileName in os.listdir(".eraser"):
        os.rename(f"./.eraser/{fileName}", f"./docs/img/{fileName}")

replaceLinksInFiles()
moveImagesToImgFolder()