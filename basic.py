import threading
import os
import time
import random


def get_reminder(dividend: int, divisor: int) -> int:
    '''
    %
    remider
    (5,3)=2g
    '''
    return dividend % divisor


def show_xor_example(x, y):
    '''
    x^0=x
    x^x=0
    '''
    return x ^ y


class PropertyExampler:
    '''
    encapsulation
    property
    '''

    def __init__(self, email):
        self.__email = email

    @property
    def email_special_api(self):
        return self.__email

    @email_special_api.setter
    def email_special_api(self, value):
        self.__email = value

    @email_special_api.getter
    def email_special_api(self):
        return self.__email

    @email_special_api.deleter
    def email_special_api(self):
        del self.__email


class CheckDataExampler:
    '''
    dynamic check attribute
    '''
    __id: int

    def __init__(self, id, is_valid_id) -> None:
        self.id = id
        self.is_valid_id = is_valid_id

    def update_id(self, new_id):
        if self.is_valid_id(new_id):
            self.id = new_id
            return True
        return False

    @staticmethod
    def check_id(id):
        if len(id) < 6:
            return False
        return True


class EnterExitExampler:
    def __init__(self) -> None:
        self.message = ["__init__"]

    def __enter__(self):
        self.message.append("__enter__")
        return self

    def __exit__(self, type, value, traceback):
        self.message.append("__exit__")


class CallExampler:
    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        return True


class ItemExampler:
    def __init__(self, key, value):
        self.classmate = {}
        self.classmate[key] = value

    def __getitem__(self, key):
        return self.classmate[key]

    def __setitem__(self, key, value):
        self.classmate[key] = value

    def __delitem__(self):
        del self.classmate


class Iterator:
    def __init__(self) -> None:
        self.index = 0
        self.max = 10

    def __next__(self):
        if self.index < self.max:
            self.index += 1
            return self.index
        else:
            raise StopIteration


def create_two_dynamic_array(raw, column):
    array = [[0]*column]*raw
    return array


class File(object):
    '''
    enter exit Example
    '''

    def __init__(self, filename, mode):
        '''
        setting filename and mode
        '''
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        '''
        open file
        '''
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, type, value, traceback):
        '''
        close file
        '''
        self.open_file.close()


class BankAccount:
    def __init__(self, name, password, credit) -> None:
        self.name = name
        self.password = password
        self.credit = credit
        self.credit_update_history = []

    def update_credit(self, change_credit):
        self.credit += change_credit


class Counter:
    def __init__(self) -> None:
        self.amount = 0
        self.lock = threading.Lock()

    def add_ten(self):
        for i in range(100000):
            self.amount += 1

    def add_ten_lock(self):
        self.lock.acquire()
        for i in range(100000):
            self.amount += 1
        self.lock.release()


def args_example(*args):
    result = []
    for i in args:
        result.append(i)
    return result


def kwargs_example(**kwargs):
    return kwargs


def three_sum(a, b, c):
    return a+b+c


def add_one(number, lock):
    print('{} start'.format(os.getpid()))
    lock.acquire()
    print('{} start to work'.format(os.getpid()))
    time.sleep(random.randint(1, 3))
    try:
        number.value += 1
    finally:
        lock.release()


def show_process():
    print(os.getpid())


def checkCashRegister(price, cash, cid):
    pass
    cash_table = {}
    cash_table['PENNY'] = 0.01
    cash_table['NICKEL'] = 0.05
    cash_table['DIME'] = 0.1
    cash_table['QUARTER'] = 0.25
    cash_table['ONE'] = 1
    cash_table['FIVE'] = 5
    cash_table['TEN'] = 10
    cash_table['TWENTY'] = 20
    cash_table['ONE HUNDRED"'] = 100

    return {"status": "OPEN", "change": [["PENNY", 0.5]]}


def produce(queue, lock):
    lock.acquire()
    try:
        print('producer {}'.format(os.getpid()))
        queue.put(os.getpid())
    finally:
        lock.release()


def consume(name, queue, lock):
    lock.acquire()
    try:
        print('consumer {} get {} '.format(name, queue.get()))
        time.sleep(random.randint(3, 5
                                  ))
    finally:
        lock.release()


def produce_pool(pool, lock):
    lock.acquire()
    try:
        print('producer {}'.format(os.getpid()))
        queue.put(os.getpid())
    finally:
        lock.release()


def consume_pool(name, pool, lock):
    lock.acquire()
    try:
        print('consumer {} get {} '.format(name, queue.get()))
        time.sleep(random.randint(3, 5
                                  ))
    finally:
        lock.release()
