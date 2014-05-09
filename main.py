#! /usr/bin/env python3

from lex import tokenize 
from parser import parse_tokenlist
from table import SymbolTable
from sys import argv

if __name__ == '__main__':
    sym = SymbolTable()
    if len(argv) <= 1:
        text="LOOP: ADD 12 3 R0;\n" +\
             "      ADD 5 R0 R1;\n" +\
             "      GOTO LOOP;;\n"
        print("Program:")
        print(text)
        token_list = tokenize(text, sym)
        s,w = parse_tokenlist(token_list)
        print("Parsed:")
        for l in s:
            print(l)
        print("Warnings:")
        for l in w:
            print(l)
    else:
        for fn in argv[1:]:
            print("File name: {}".format(fn))
            with open(fn) as f:
                token_list = tokenize(f.read(), sym)
                s,w = parse_tokenlist(token_list)
                print("Parsed:")
                for l in s:
                    print(l)
                print("Warnings:")
                for l in w:
                    print(l)

            
