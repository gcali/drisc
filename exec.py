#! /usr/bin/env python3

from mem import Memory

class Instruction():
    def __init__(self, op_code:int, *args:int):
        self.op_code = op_code
        self.args = args

class CPU():
    def __init__(self, start_ic = 0):
        self.ic = start_ic
        self.registers = [0 for i in range(64)]

    def execute_next(self, memory:Memory):
        next_instruction = memory.get_value(self.ic)

        
