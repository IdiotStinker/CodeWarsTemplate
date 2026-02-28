from pathlib import Path
import os

starterCode = "with open(\"input.txt\", \"r\") as f:\n\tINPUT = f.read().split(\"\\n\")"

def create(probCount = 30):
    for i in range(probCount):
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
        if file in [".git", ".gitattributes", "prob_checker.py", 
            "exampleDirectoryProb.py"]: continue
        if "prob" not in file and ".py" not in file: continue
        os.remove(os.getcwd() + "\\" + file)

create()
#restart()