#! /usr/bin/env python3

from sys import argv
from misc import str_list, is_number
from table import SymbolTable

class Token:
    def __init__(self, token_name:str, token_value:str=None, line_number:int=None):
        """Token constructor
            
        Attributes
            token_name  The name of the token (eg identifier)
            token_value An (optional) attribute (eg R5)
            line_number The line number where the token was found
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
             start_line_number:int=1) -> "list(Token)":
    """Create a list of tokens from a statement
    
    Args
        statement   The statement to be tokenized
    """
    l = []
    current_token = []
    line_number = start_line_number
    #statement = statement.lower()
    for c in statement:
        if c.isalnum() or c in ["<",">","=","!"]:
            current_token.append(c)
        else:
            if c == "\n":
                line_number += 1
            if current_token:
                string = "".join(current_token)
                l.append(_token_from_name(string, table, line_number))
                current_token = []
            if c == ";" or c == ":":
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
    elif token_string[0].lower() == "r":
        token_id = "identifier"
    else:
        token_id = "label"
    return Token(token_id, token_string, line_number=line_number)
        
if __name__ == "__main__":
    args = ["START:ADD 10 9 R3;\nADD R3 5 R5;\nGOTO  START"] + argv[1:]

    table = SymbolTable()

    print(args)
    for arg in args:
        print(str_list(tokenize(arg, table)))
