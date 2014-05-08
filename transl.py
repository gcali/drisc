#! /usr/bin/env python3

from lex import Token
from unit import Unit
from misc import str_list

class LookupTable():
    def __init__(self):
        self.table = dict()

    def add(self, entry_a, entry_b):
        self.table[entry_a] = entry_b
        self.table[entry_b] = entry_a

    def remove(self, entry):
        dict.__delitem__(self.table, self.table[entry])
        dict.__delitem__(self.table, entry)

    def translate(self, entry):
        return self.table[key]

class Arg:
    def __init__(self, value:str, is_register:bool=True, is_label:bool=False):
        self.value = value
        self.is_register = is_register
        self.is_label = is_label
    
    def is_register(self) -> bool:
        return self.is_register

    def get_value(self) -> str:
        return self.value

    def __str__(self):
        if self.is_label:
            d = "(L)"
        elif self.is_register:
            d = "(R)"
        else:
            d = ""
        return "{}{}".format(self.value,d)

class Statement:
    """Class to represent an abstract statement

        Attributes
            op          Operation identifier
            args        Arguments of the statement
            label       Optional label of the statement
            line_number Line number of the statement
    """
    def __init__(self, line_number=None, op=None, *args, label=None):
        """Constructor
        
        Sets the attributes of the class
        """
        self.op = op
        self.args = [a for a in args]
        self.label = label
        self.line_number = line_number

    def is_new(self) -> bool:
        if self.op or self.args or self.label or self.line_number:
            return False
        else:
            return True
    
    def to_unit_value(self) -> Unit:
        raise NotImplementedError

    def __str__(self):
        if self.label != None:
            l = "(L-{})".format(self.label)
        else:
            l = ""
        a = str_list(self.args)
        if self.line_number != None:
            n = "{}: ".format(str(self.line_number))
        else:
            n = ""
        return "{}{} {} {}".format(n,l,self.op,a)
        

if __name__ == '__main__':
    Statement("a", "b", "c", "d")
