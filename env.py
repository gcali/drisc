#! /usr/bin/env python3

from transl import LookupTable

class Env():
    def __init__(self, binding_list = []):
        self.bindings = dict()
        self.next_id = 0
        for elem in binding_list:
            self.bind(elem)

    def bind(self, elem) -> int:
        if elem in self.bindings:
            return self.bindings[elem]
        else:
            self.bindings[elem] = self.next_id
            self.next_id += 1
            return self.next_id-1

    def __contains__(self, item):
        return item in self.bindings

    def __str__(self) -> str:
        ret_list = ["{} -> {}".format(key, self.bind(key))\
                    for key in sorted(self.bindings.keys())]
        return "\n".join(ret_list)
        
        
if __name__ == '__main__':
    e = Env(["R0", "R1", "R2"])
    print(e)
