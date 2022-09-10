

class A():
    def __init__(self):
        print("A.__init__")
        self.val = None

    def __str__(self):
        print("A.__str__")
        return "{0!r} {1}".format(self, self.val)