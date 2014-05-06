#! /usr/bin/env python3

from unit import Unit

class Memory():
    def __init__(self, size=2**8):
        self.memory_list = dict()
        self.size = size
        self._digits = 8

    def set_value(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("memory index out of bounds")
        self.memory_list[index] = Cell(value)

    def get_value(self, index) -> int:
        if index < 0 or index >= self.size:
            raise IndexError("memory index out of bounds")
        try:
            return self.memory_list[index].get_value()
        except KeyError:
            return Cell(0)

    def list_defined(self) -> "Iter":
        for key in self.memory_list.keys():
            yield key

    #def table(self) -> str:
    #    ret_string = ["-"*
    #    for key in self.list_defined():

    def __str__(self):
        format_string = "{{:#0{}x}} -> {{}}".format(self._digits+2)
        #+2 for the 0x
        ret_list = [ format_string.format(key, self.get_value(key)) for key in self.list_defined()]
        return "\n".join(ret_list)
            
            

class Cell():
    def __init__(self, value=0):
        self.value = Unit(value)

    def get_value(self):
        return self.value

if __name__ == '__main__':
    m = Memory()
    print("Empty memory")
    print(m)

    m.set_value(3, 12)
    m.set_value(3, 5)
    m.set_value(5, 5)
    print("Not empty memory")
    print(m)
