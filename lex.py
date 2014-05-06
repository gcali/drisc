#! /usr/bin/env python3

from sys import argv
from misc import str_list, is_number

class SymbolTable():
    def __init__(self, operators=["ADD", "MUL", "STORE", "LOAD", "GOTO"],
                       keywords=[";"]):
        self.table = dict()
        self.last_id = -1
        self.keywords = keywords
        self.operators = operators

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
        return string in self.operators

    def is_keyword(self, string:str) -> bool:
        return string in self.keywords

    def is_constant(self, string:str) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False


class Token:
    def __init__(self, token_name:str, token_value:str=None, line_number:int=None):
        """Token constructor
            
        Attributes
            token_name  The name of the token
            attribute   An (optional) attribute
        """
        self.token_name = token_name
        self.token_value = token_value
        self.line_number = line_number

    def __str__(self) -> str:
        s_list = [str(self.token_name), str(self.token_value)]
        if self.line_number != None:
            s_list.append("ln:" + str(self.line_number))
        return "<" + ",".join(s_list) + ">"


def tokenize(statement:str, table:SymbolTable,
             start_line_number:int=0) -> "list(Token)":
    """Create a list of tokens from a statement
    
    Args
        statement   The statement to be tokenized
    """
    l = []
    current_token = []
    line_number = start_line_number
    statement = statement.lower()
    for c in statement:
        if c.isalnum():
            current_token.append(c)
        else:
            if c == "\n":
                line_number += 1
            if current_token:
                string = "".join(current_token)
                l.append(_token_from_name(string, table, line_number))
                current_token = []
            if c == ";":
                l.append(_token_from_name(c, table, line_number))
    if current_token:
        l.append(_token_from_name("".join(current_token), table))
    return l

def _token_from_name(token_string:str, table:SymbolTable, line_number:int=None) -> Token:
    """Returns the correct token from the name
    """
    if table.is_keyword(token_string):
        token_id = "keyword"
    elif table.is_operator(token_string):
        token_id = "operator"
    elif table.is_constant(token_string):
        token_id = "constant"
    else:
        token_id = "identifier"
    return Token(token_id, token_string, line_number=line_number)
        
if __name__ == "__main__":
    args = ["ADD 10 9 R3;\nADD R3 5 R5;"] + argv[1:]

    table = SymbolTable()

    for arg in args:
        print(str_list(tokenize(arg, table)))
