import os

OUTPUTS = "./tests/outputs/"
ORIGINALS = "./tests/originals/"


outputs = os.listdir(OUTPUTS)
originals = os.listdir(ORIGINALS)

all = len(originals)
passed = 0


for o in originals:
    original = ""
    path = f"{ORIGINALS}{o}".replace("/", "\\")
    file = open(path, "r")
    original = file.read()
    file.close()

    try:
        path = f"{OUTPUTS}{o}".replace("/", "\\")
        file = open(path, "r")
        output = file.read()
        file.close()
    except:
        print("File not found in OUTPUTS: ", o)
        continue

    if original != output:
        print("Files diff: ", o)
    else:
        passed += 1


print(f"Files passed: {passed}/{all}")
