import os
import shutil
from .lexer import *
from .parser import *
import subprocess

dir = os.getcwd()

class kite_build:
    def __init__(self, arsg) -> None:
        self.dir = os.getcwd()
        self.arsg = arsg
        self.command = self.arsg[1]
        self.subcommand = None
        if self.command == "init":
            self.subcommand = self.arsg[2]
            self.kite_build_init(self.subcommand)
        elif self.command == "remove":
            self.subcommand = self.arsg[2]
            self.kite_build_remove(self.subcommand)
        elif self.command == "compile":
            self.kite_build_compile()

    def kite_build_remove(self, project_name) -> None:
        self.project_name = project_name
        shutil.rmtree(f"{self.project_name}")
        print("Project removed!")

    def kite_build_init(self, project_name) -> None:
        self.project_name = project_name
        os.mkdir(f"{self.project_name}")
        os.mkdir(f"{self.project_name}/build")
        os.mkdir(f"{self.project_name}/build/tokens")
        os.mkdir(f"{self.project_name}/build/cargo")
        os.mkdir(f"{self.project_name}/library")
        os.mkdir(f"{self.project_name}/src")
        subprocess.run(
            ["cargo", "new", "cargo_project"],
            cwd=self.dir+f"/{self.project_name}/build/cargo",
        )
        with open(f"{self.project_name}/src/main.ki", "w") as f:
            pass
        with open(f"{self.project_name}/kiproject.toml", "w") as f:
            pass
        print("===========================\nKite project created!")

    def kite_build_compile(self) -> None:
        files = os.listdir("src")
        for f in files:
            file = open(f"src/{f}", "r").readlines()
            lexer(file, f)
        parse = Parser()
        parse.compileRust()


class kite_debug:
    def __init__(self, arsg) -> None:
        self.arsg = arsg
        self.command = self.arsg[1]
        if len(self.arsg) >= 3:
            self.subcommand = self.arsg[2]
        if self.command == "lexer":
            self.kite_debug_lexer(self.subcommand)
        elif self.command == "readfile":
            self.kite_debug_readfile(self.subcommand)
        elif self.command == "parser":
            self.kite_debug_parser()

    def kite_debug_lexer(self, filename) -> None:
        file = open(f"src/{filename}", "r").readlines()
        lexer(file, filename, debug=True)

    def kite_debug_parser(self) -> None:
        Parser("hey")

    def kite_debug_readfile(self, filename) -> None:
        file = open(f"src/{filename}", "r").readlines()
        for i, line in zip(range(len(file)), file):
            print(f"{i+1}| {line.replace('\n', '')}")
