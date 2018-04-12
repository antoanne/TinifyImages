import tinify
import os, glob
tinify.key = "<KEY>"
# tinify.proxy = "http://user:pass@192.168.0.1:8080"

diretorio = os.path.join('<FOLDER>')

for root, dirs, files in os.walk(diretorio):
    for file in files:
        if file.endswith(".jpg"):
            currentFile = os.path.join(root, file)
            newRoot = root.replace('<FROM-FODER>','<TO-FOLDER>')
            optimizedFile = os.path.join(newRoot, file)
            print(currentFile)
            source = tinify.from_file(currentFile)
            if not os.path.exists(newRoot):
                os.makedirs(newRoot)
            source.to_file(optimizedFile)
            print(optimizedFile)