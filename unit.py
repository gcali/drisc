#! /usr/bin/env python3

_modulo_value = 2**8

class Unit(int):
    def __new__(cls,arg):
        return super().__new__(cls,arg % (_modulo_value))

    def __str__(self):
       return "{:#010x}".format(self)

    def __add__(self,other):
        return Unit(super().__add__(other) % _modulo_value)

    def __mul__(self,other):
        return Unit(super().__mul__(other) % _modulo_value)

    def __sub__(self,other):
        return Unit(super().__sub__(other) % _modulo_value)

    def __div__(self,other):
        return Unit(super().__div__(other) % _modulo_value)

    def __floordiv__(self,other):
        return Unit(super().__floordiv__(other) % _modulo_value)

if __name__ == '__main__':
    print("Modulo {}".format(2**8))
    print(Unit(10))
    print(Unit(100))
    print(Unit(2**8))
    print(Unit(2**8+10))
    print(Unit(2**7) + Unit(2**7) + Unit(12))
    print(Unit(2**6) * Unit(2))
