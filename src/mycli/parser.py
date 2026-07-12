import os
import subprocess
import ast

files = os.listdir("build/tokens")
tokenlist = files.copy()

defaultFunctions = """
#![allow(warnings)]

use std::fmt::Debug;

fn print(text: &str) {
    println!("{}", text);
}

fn str<T: Debug>(var: T) -> String {
    format!("{:?}", var)
}
"""

class Parser:
    def __init__(self):
        self.dir = os.getcwd()
        self.files = []
        for file in tokenlist:
            with open(f"build/tokens/{file}", "r") as f:
                items = ast.literal_eval(f.read())
                self.files.append(items)
        print(self.files)
        self.writeRust()

    def writeRust(self):
        for filename, file in zip(tokenlist, self.files):
            filename = filename[:-7]
            with open(f"build/cargo/cargo_project/src/{filename}.rs", "w") as f:
                f.write(defaultFunctions)
            with open(f"build/cargo/cargo_project/src/{filename}.rs", "a") as f:
                for token in file:
                    if token[0] == "OPEN_SCOPE":
                        f.write(" { ")
                    elif token[0] == "CLOSE_SCOPE":
                        f.write(" } ")
                    elif token[0] == "FUNC":
                        f.write(" fn ")
                    elif token[0] == "IF":
                        f.write(" if ")
                    elif token[0] == "ELSE":
                        f.write(" else ")
                    elif token[0] == "ELIF":
                        f.write(" elif ")
                    elif token[0] == "MUT_VAR":
                        f.write(" let mut ")
                    elif token[0] == "IDENTIFIER":
                        if token[1] != ":":
                            f.write(token[1])

    def compileRust(self):
        subprocess.run(
            ["cargo", "build"],
            cwd=self.dir + f"/build/cargo/cargo_project"
        )
        subprocess.run(
            ["./cargo_project"],
            cwd=self.dir + f"/build/cargo/cargo_project/target/debug"
        )

