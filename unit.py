#! /usr/bin/env python3

_modulo_value = 2**8

from math import log

def _digits(n:int) -> int:
    return int(log(n,2))
    

class Unit(int):
    def __new__(cls,val,mod=_modulo_value):
        ret = super().__new__(cls,val % (mod))
        ret.mod = _modulo_value
        ret.dig = _digits(ret.mod)
        return ret

    def int_str(self):
        return super().__str__()

    def __str__(self):
        form_str = "{{:#0{}x}}".format(self.dig+2)
        return form_str.format(self)
       #return "{:#010x}".format(self)

    def __add__(self,other):
        return Unit(super().__add__(other) % self.mod,self.mod)

    def __mul__(self,other):
        return Unit(super().__mul__(other) % self.mod,self.mod)

    def __sub__(self,other):
        return Unit(super().__sub__(other) % self.mod,self.mod)

    def __div__(self,other):
        return Unit(super().__div__(other) % self.mod,self.mod)

    def __floordiv__(self,other):
        return Unit(super().__floordiv__(other) % self.mod,self.mod)

if __name__ == '__main__':
    print("Modulo {}".format(_modulo_value))
    print(Unit(10))
    print(Unit(100))
    print(Unit(2**8))
    print(Unit(2**8+10))
    print(Unit(2**7) + Unit(2**7) + Unit(12))
    print(Unit(2**6) * Unit(2))
