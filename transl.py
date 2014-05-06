#! /usr/bin/env python3

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
