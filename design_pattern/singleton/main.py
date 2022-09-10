



import example_a

class SingletonObject(object): 
    instance = None
    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = example_a.A()
        return SingletonObject.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)



if __name__ == "__main__":

    # object 1
    tester_1 = SingletonObject()
    tester_1.val = "tester1"
    print("test1: ", tester_1)  # tester1
    
    # object 2
    tester_2 = SingletonObject()
    print("test1: ", tester_1)  # tester1
    tester_2.val = "tester2"
    print("test1: ", tester_1)  # tester2
    print("test2: ", tester_2)  # tester2