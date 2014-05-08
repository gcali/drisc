#! /usr/bin/env python3

class SymbolTable():
    def __init__(self, operators=["ADD", "MUL", "SUB", "DIV",
                                  "LOAD", "STORE",
                                  "IF<", "IF>", "IF<=", "IF>=",
                                  "IF=", "IF!=", "GOTO"
                                  ],
                       keywords=[";",":"]):
        self.table = dict()
        self.last_id = -1
        self.keywords = [k.lower() for k in keywords]
        self.operators = [op.lower() for op in operators]

    def get_id(self, entry:str) -> int:
        """Returns the id of the token
        """
        if entry in self.table:
            return self.table[entry]
        else:
            self.last_id += 1
            self.table[entry] = self.last_id
            return self.last_id

    def is_operator(self, string:str) -> bool:
        return string.lower() in self.operators

    def is_keyword(self, string:str) -> bool:
        return string.lower() in self.keywords

    def is_constant(self, string:str) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False


