#! /usr/bin/env python3

def str_list(l:list, separator:str=", ", lbracket="[", rbracket="]") -> str:
    return "{0}{1}{2}".format(lbracket,
                              separator.join([str(el) for el in l]),
                              rbracket)

def is_number(s:str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    print(str_list(["Prova","di","stampa"], lbracket="", rbracket="", separator=" "))
