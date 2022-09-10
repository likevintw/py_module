

import prototype

class A(prototype.Prototype):
    def __init__(self): print("A initial")
    def say_hello(self): print("Hello A")

class B(prototype.Prototype):
    def __init__(self): print("B initial")
    def say_hello(self): print("Hello B")

class CreateObject:
    def __init__(self, _object_unit):
        self.unit = _object_unit
    def build_unit(self, _para):
        return self.unit.get(_para).clone()


# unit test
if __name__ == "__main__":
    object_unit = {1:A(),2:B()} # only create object for once
    creater = CreateObject(object_unit)


    print("ask an object A for a1")
    a1 = creater.build_unit(1)
    a1.say_hello()

    print("ask an object A for a2")
    a2 = creater.build_unit(1)
    a2.say_hello()

    print("ask an object B for b1")
    b1 = creater.build_unit(2)
    b1.say_hello()

    print("ask an object B for b2")
    b2 = creater.build_unit(2)
    b2.say_hello()
