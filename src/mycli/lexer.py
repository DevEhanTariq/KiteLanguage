from pip._internal.utils import appdirs

from .tokens import *
import sys

tokens = {
    "OPEN_SCOPE": None,
    "CLOSE_SCOPE": None,
    "MUT_VAR": None
}

class lexer:
    def __init__(self, file, filename: str, debug=False) -> None:
        self.filename = filename
        self.file = file
        self.debug = debug

        self.term_replace()
        self.tokenise()

    def term_replace(self):
        newfile = []
        for line in self.file:
            line = line.replace("    ", " <indented> ")
            line = line.replace(":", " : ")
            line = line.replace("(", " ( ")
            line = line.replace(")", " ) ")
            line = line.replace("[", " [ ")
            line = line.replace("]", " ] ")
            line = line.replace("{", " { ")
            line = line.replace("}", " } ")
            line = line.replace(",", " , ")
            line = line.replace("+", " + ")
            line = line.replace("-", " - ")
            line = line.replace("*", " * ")
            line = line.replace("/", " / ")
            line = line.replace("AND", " AND ")
            line = line.replace("OR", " OR ")
            line = line.replace("NOT", " NOT ")
            line = line.replace("NAND", " NAND ")
            line = line.replace("NOR", " NOR ")
            line = line.replace("XOR", " XOR ")
            line = line.replace("/", " / ")
            line = line.replace("rust<<", " rust<< ")
            line = line.replace("asm<<", " asm<< ")
            line = line.replace(">>", " >> ")
            line += " ; "
            newfile.append(line)

        newfile.append(" <END> ")

        self.file = newfile

    def tokenise(self):
        vars = {}
        tokens = []
        level = 0
        for line in self.file:
            line = line.split()
            if len(line) != 0:
                while line[-1] == "<indented>":
                    line = line[:-1]
            if line == []:
                continue

            lastLevel = level
            level = 0
            for component in line:
                # Scopes
                if component == "<indented>":
                    level += 1
            if level > lastLevel:
                tokens.append(OPEN_SCOPE())
            elif level < lastLevel:
                change = lastLevel - level
                for i in range(change):
                    tokens.append(CLOSE_SCOPE())

            for component in line:
                # Vars
                if component == "var":
                    tokens.append(MUT_VAR())
                    continue

                # Functions
                elif component == "func":
                    tokens.append(FUNC())
                    continue

                # Statements
                elif component == "if":
                    tokens.append(IF())
                    continue

                elif component == "else":
                    tokens.append(ELSE())
                    continue

                elif component == "elif":
                    tokens.append(ELIF())
                    continue

                elif component == "<indented>":
                    continue

                if component != "<END>":
                    tokens.append(IDENTIFIER(value=str(component)))

            with open(f"build/tokens/{self.filename[:-3]}.tokens", "w") as f:
                f.write(str(tokens))

            if self.debug:
                print(tokens)