import os
import shutil

class kite_init:
    def __init__(self, project_name) -> None:
        self.project_name = project_name
        os.mkdir(f"{self.project_name}")
        os.mkdir(f"{self.project_name}/libraries")
        with open(f"{self.project_name}/main.ki", "w") as f:
            pass
        with open(f"{self.project_name}/kiproject.toml", "w") as f:
            pass
        print("Kite project created!")

class kite_remove:
    def __init__(self, project_name) -> None:
        self.project_name = project_name
        shutil.rmtree(f"{self.project_name}")
        print("Project removed!")

class kite_build:
    def __init__(self, arsg) -> None:
        self.command = arsg[1]
        self.subcommand = arsg[2]
        if self.command == "init":
            kite_init(self.subcommand)
        elif self.command == "remove":
            kite_remove(self.subcommand)
            
class kite_debug:
    def __init__(self, arsg) -> None:
        self.arsg = arsg
