
'''
time elapse
'''


import time

# decorator 1


class ShowResult():

    def __init__(self, _function):
        print("A __init__ start")
        self.function = _function
        print("A __init__ end")

    def __call__(self, *_function):
        print("A __call__ start")
        print("A Before Function")
        result = self.function(*_function)  # execute function
        print("A After Function")
        print("A The result is: {}".format(result))
        print("A __call__ end")
        return result

# decorator 2


class TimeElapse():

    def __init__(self, _function):
        print("B __init__ start")
        self.function = _function
        print("B __init__ end")

    def __call__(self, *_function):
        print("B __call__ start")
        print("B Before Function")
        start_time = time.time()
        result = self.function(*_function)  # execute function
        print("B After Function")
        print("B Time elapse {} s for input = {}".format(
            n, time.time()-start_time))
        print("B __call__ end")
        return result


@ShowResult  # A
@TimeElapse  # B
def fibonacci_number(_n):   # function
    print("F fibonacci_number start")
    if _n <= 1:
        return _n
    first, second = 1, 1
    for i in range(2, _n):
        first, second = second, second+first
    print("F fibonacci_number end")
    return second


if __name__ == '__main__':
    n = 100
    print(n, fibonacci_number(n))

    # result
    """
    B __init__ start
    B __init__ end
    A __init__ start
    A __init__ end
    A __call__ start
    A Before Function
    B __call__ start
    B Before Function
    F fibonacci_number start
    F fibonacci_number end
    B After Function
    B Time elapse 100 s for input = 2.3126602172851562e-05
    B __call__ end
    A After Function
    A The result is: 354224848179261915075
    A __call__ end
    100 354224848179261915075
    """
