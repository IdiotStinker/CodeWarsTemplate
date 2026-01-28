from pathlib import Path
import random
import os

starterCode = "with open(\"input.txt\", \"r\") as f:\n\tINPUT = f.read().split(\"\\n\")"

def create(num = 30):
    for i in range(num):
        if i < 10:
            file = Path("prob0" + str(i) + ".py")
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(starterCode)
        else:
            file = Path("prob" + str(i) + ".py")
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(starterCode)

def restart():
    for file in os.listdir():
        if Path(__file__.split("\\")[-1])==Path(file): continue
        if file in [".git", ".gitattributes"]: continue
        os.remove(os.getcwd() + "\\" + file)

create()
#restart()