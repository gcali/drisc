#! /usr/bin/env python3

from lex import Token
from transl import Statement, Arg

from lex import tokenize
from table import SymbolTable

from misc import str_list

class ParsingError(Exception):
    pass

def _create_parse_error(line_number:int, message:str, token:str)\
                        -> ParsingError:
    return ParsingError("(ParseError) l{}: {}\nToken: {}".format(
        line_number, message, token
    ))

def _create_parse_warning(line_number:int, message:str) -> str:
    return "(ParseWarning) l{}: {}".format(line_number, message)

def parse_tokenlist(token_list:"list(token)")\
    -> ("list(statements)","list(str)"):
    """Parse a list of tokens

    Returns a tuple: the first element is the list of parsed statements,
    the second one is a list of warnings found during compilation
    """
    curr_statement = Statement()
    statement_list = []
    warnings_list = []
    label_table = dict()
    is_in_args = False
    next_is_semicolon = False
    next_is_colon = False
    for t in token_list:
        if next_is_semicolon and t.token_value != ";":
            raise _create_parse_error(t.line_number,
                                      "; expected",
                                      t.token_value)
        elif next_is_colon and t.token_value != ":":
            raise _create_parse_error(t.line_number,
                                      ": expected",
                                      t.token_value)
        elif t.token_name == "label":
            if not is_in_args and not curr_statement.is_new():
                raise _create_parse_error(t.line_number,
                                          "Label must be at start of "+
                                          "instruction or in args",
                                          t.token_value) 
            elif not is_in_args:
                curr_statement.label = t.token_value
                next_is_colon = True
            else:
                curr_statement.args.append(Arg(t.token_value,
                                               is_register=False,
                                               is_label=True))
                next_is_semicolon = True
        elif t.token_name == "operator":
            if is_in_args:
                raise _create_parse_error(t.line_number,
                                          "operator given when arguments "+
                                          "were expected",
                                          t.token_value)
            else:
                curr_statement.op = t.token_value
                is_in_args = True
        elif t.token_name == "identifier":
            if not is_in_args:
                raise _create_parse_error(t.line_number,
                                          "identifier not expected",
                                          t.token_value)
            else:
                curr_statement.args.append(Arg(t.token_value,
                                               is_register=True,
                                               is_label=False))
        elif t.token_name == "constant":
            if not is_in_args:
                raise _create_parse_error(t.line_number,
                                          "constant not expected",
                                          t.token_value)
            else:
                curr_statement.args.append(Arg(t.token_value,
                                               is_register=False,
                                               is_label=False))
        elif t.token_name == "keyword" and t.token_value == ":":
            if not next_is_colon:
                raise _create_parse_error(t.line_number,
                                          "colon expected",
                                          t.token_value)
            else:
                next_is_colon = False

        elif t.token_name == "keyword" and t.token_value == ";":
            curr_statement.line_number = t.line_number
            statement_list.append(curr_statement)
            if not curr_statement.op:
                warnings_list.append(_create_parse_warning(
                    t.line_number, "empty statement"
                ))
            curr_statement = Statement()
            next_is_semicolon = False
            is_in_args = False

    if not curr_statement.is_new():
        warnings_list.append(_create_parse_warning(
            -1, "last statement not empty"
        ))
    return (statement_list,warnings_list)

if __name__ == '__main__':
    text="LOOP: ADD 12 3 R0;\n" +\
         "      ADD 5 R0 R1;\n" +\
         "      GOTO LOOP;;\n"
    print("Program:")
    print(text)
    token_list = tokenize(text, SymbolTable())
    s,w = parse_tokenlist(token_list)
    print("Parsed:")
    for l in s:
        print(l)
    print("Warnings:")
    for l in w:
        print(l)
