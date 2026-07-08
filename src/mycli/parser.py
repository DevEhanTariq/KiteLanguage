from .tokens import *

class parseFile:
    def __init__(self, file) -> None:
        self.fileContent = []
        self.fileTokens = []
        lines = open(file, "r").readlines()

        for line in lines:
            line = line.replace("(", " ( ")
            line = line.replace(")", " ) ")
            line = line.replace("[", " [ ")
            line = line.replace("]", " ] ")
            line = line.replace("{{", " <curly/ ")
            line = line.replace("}}", " /curly> ")
            line = line.replace("{", " { ")
            line = line.replace("}", " } ")
            line = line.strip().split()
            if line != []:
                self.fileContent.append(line)

        print(self.fileContent)

    def tokenise(self):
        for line in self.fileContent:
            currentLine = []
            for component in line:
                if component[0] == '"' and component[-1] == '"':
                    currentLine.append(string())
                    currentLine[-1].value = component[1:-1]
                else:
                    try:
                        val = float(component)
                        currentLine.append(kfloat())
                        currentLine[-1].value = val
                    except:
                        try:
                            val = int(component)
                            currentLine.append(integer())
                            currentLine[-1].value = val
                        except:
                            pass

            if currentLine == []:
                continue
            self.fileTokens.append(currentLine)
        print(self.fileTokens)

def parse(arsg) -> None:
    main = parseFile(arsg[1])
    main.tokenise()

def main() -> None:
    pass

if __name__ == "__main__":
    pass