#! /usr/bin/env python3

from sys import argv
from misc import str_list, is_number

class SymbolTable():
    def __init__(self, keywords=["ADD", "MUL", "STORE", "LOAD", ";"]):
        self.table = dict()
        self.last_id = -1
        self.keywords = keywords

    def get_id(self, entry:str) -> int:
        """Returns the id of the token
        """
        if entry in self.table:
            return self.table[entry]
        else:
            self.last_id += 1
            self.table[entry] = self.last_id
            return self.last_id

    def needs_id(self, token_name:str) -> bool:
        """Returns true iff the token needs an id
        """
        if token_name in self.keywords:
            return False
        if is_number(token_name):
            return False
        return True
        

class Token:
    def __init__(self, token_name:str, attribute:str=None):
        """Token constructor
            
        Attributes
            token_name  The name of the token
            attribute   An (optional) attribute
        """
        self.token_name = token_name
        self.attribute = attribute

    def __str__(self) -> str:
        s_list = [str(self.token_name)]
        if self.attribute != None:
            s_list.append(str(self.attribute))
        return "<" + ",".join(s_list) + ">"


def lex_analyze(statement:str, table:SymbolTable) -> "list(Token)":
    """Create a list of tokens from a statement
    
    Args
        statement   The statement to be tokenized
    """
    l = []
    current_token = []
    for c in statement:
        if c.isalnum():
            current_token.append(c)
        elif current_token:
            l.append(_token_from_name("".join(current_token), table))
            current_token = []
        if c == ";":
            l.append(Token(c))
    if current_token:
        l.append(_token_from_name("".join(current_token), table))
    return l

def _token_from_name(token_name:str, table:SymbolTable) -> Token:
    """Returns the correct token from the name
    """
    if table.needs_id(token_name):
        return Token(token_name, table.get_id(token_name))
    else:
        return Token(token_name)
        
if __name__ == "__main__":
    args = ["ADD 10 9 R3;", "ADD R3 5 R5;"] + argv[1:]

    table = SymbolTable()

    for arg in args:
        print(str_list(lex_analyze(arg, table)))
