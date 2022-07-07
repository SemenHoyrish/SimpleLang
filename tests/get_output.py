import os

PATHS = ["./examples/", "./tests/"]
OUTPUT = "./tests/outputs/"
INPUT = "./tests/inputs/"

#.\sl.exe .\examples\get_set.sl < .\tests\inputs\get_set.input > .\tests\outputs\get_set.sl.txt

inputs = os.listdir(INPUT)
for path in PATHS:
    content = os.listdir(path)
    for item in content:
        if not item.endswith(".sl"):
            continue
    
        item = item[0:len(item) - 1 - 2]

        
        cmd = f"./sl.exe {path}{item}.sl"
        if f"{item}.input" in inputs:
            cmd += f" < {INPUT}{item}.input"
        
        cmd += f" > {OUTPUT}{item}.output"
        
        
        cmd = cmd.replace("/", "\\")

        print(cmd)
        os.system(cmd)

