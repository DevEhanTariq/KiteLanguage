# ============================================================= SCOPES

class OPEN_SCOPE:
    def __init__(self, value=None):
        self.token = "OPEN_SCOPE"
        self.value = value

    def __str__(self):
        return str((self.token, self.value))

    def __repr__(self):
        return self.__str__()

class CLOSE_SCOPE:
    def __init__(self, value=None):
        self.token = "CLOSE_SCOPE"
        self.value = value

    def __str__(self):
        return str((self.token, self.value))

    def __repr__(self):
        return self.__str__()

# ============================================================= VARS

class MUT_VAR:
    def __init__(self, value=None):
        self.token = "MUT_VAR"
        self.value = value

    def __str__(self):
        return str((self.token, self.value))

    def __repr__(self):
        return self.__str__()

# ============================================================= STATEMENTS

class FUNC:
    def __init__(self, value=None):
        self.token = "FUNC"
        self.value = value

    def __str__(self):
        return str((self.token, self.value))

    def __repr__(self):
        return self.__str__()

class IF:
    def __init__(self, value=None):
        self.token = "IF"
        self.value = value

    def __str__(self):
        return str((self.token, self.value))

    def __repr__(self):
        return self.__str__()

class ELSE:
    def __init__(self, value=None):
        self.token = "ELSE"
        self.value = value

    def __str__(self):
        return str((self.token, self.value))

    def __repr__(self):
        return self.__str__()

class ELIF:
    def __init__(self, value=None):
        self.token = "ELIF"
        self.value = value

    def __str__(self):
        return str((self.token, self.value))

    def __repr__(self):
        return self.__str__()

# ============================================================= IDENTIFIER

class IDENTIFIER:
    def __init__(self, value=None):
        self.token = "IDENTIFIER"
        self.value = value

    def __str__(self):
        return str((self.token, self.value))

    def __repr__(self):
        return self.__str__()