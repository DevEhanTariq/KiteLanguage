import os
import shutil

class kinit:
    def __init__(self, arsg) -> None:
        self.direct = arsg[1]
        os.mkdir(f"{self.direct}")
        os.mkdir(f"{self.direct}/library")
        with open(f"{self.direct}/main.ki", "w") as f:
            pass
        with open(f"{self.direct}/kiproject.toml", "w") as f:
            pass
        print("Kite project created!")

class kremove:
    def __init__(self, arsg) -> None:
        self.direct = arsg[1]
        yn = input("Do you really want to remove this project? [y/n]: ").lower()
        if yn == "y":
            shutil.rmtree(f"{self.direct}")
            print("Project removed!")
        else:
            print("Process cancelled!")
