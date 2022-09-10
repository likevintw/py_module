

class A:
    def __init__(self):
        self.message = []
        self.__private()
        self.public()

    def __private(self):
        self.message.append("A.private()")

    def public(self):
        self.message.append("A.public()")


class B(A):
    def __private(self):
        self.message.append("B.private()")

    def public(self):
        self.message.append("B.public()")


class NewDemo:
    def __init__(self) -> None:
        pass

    def __new__(self): print("__new__")


class StructureDemo:
    def __init__(self, callback) -> None:
        self.callback = callback

    def __call__(self):
        return "__call__"

    def __del__(self):
        self.callback("__del__")


class DemoClass:
    def __init__(self, callback_init, callback_new, callback_del) -> None:
        self.callback_init = callback_init
        self.callback_new = callback_new
        self.callback_del = callback_del
        self.callback_init("__init__")

    def __call__(self):
        return "__call__"

    def __new__(self, *args, **kwargs):  # unfinished
        pass

    def __del__(self):
        self.callback_del("__del__")
