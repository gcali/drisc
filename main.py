from lex import tokenize

from parser import parse_tokenlist

if __name__ == '__main__':
    text="LOOP: ADD 12 3 R0;\n" +\
         "      ADD 5 R0 R1;\n" +\
         "      GOTO LOOP;;\n"
    print("Program:")
    print(text)
    token_list = tokenize(text, SymbolTable())
    print(str_list(token_list))
    s,w = parse_tokenlist(token_list)
    print("Parsed:")
    for l in s:
        print(l)
    print("Warnings:")
    for l in w:
        print(l)
