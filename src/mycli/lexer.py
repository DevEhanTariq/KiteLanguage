class lexer:
    def __init__(self, file) -> None:
        self.file = file
        self.term_replace()

    def term_replace(self):
        newfile = []
        for line in self.file:
            line = line.replace("    ", " <indented> ")
            line = line.replace("(", " ( ")
            line = line.replace(")", " ) ")
            line = line.replace("[", " [ ")
            line = line.replace("]", " ] ")
            line = line.replace("{", " { ")
            line = line.replace("}", " } ")
            line = line.replace("rust<<", " rust<< ")
            line = line.replace("asm<<", " asm<< ")
            line = line.replace(">>", " >> ")
            newfile.append(line)

        self.file = newfile

    def tokenise(self):
        pass
