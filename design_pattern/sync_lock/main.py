import threading
import time

def function_example():
    def fun_sub():
        lock.acquire()
        print('worker:',t.name)
        time.sleep(0.1)
        lock.release()

    lock = threading.Lock()

    thread_list = []
    for thread in range(5):
        t = threading.Thread(target=fun_sub)
        t.start()
        thread_list.append(t)

    for t in thread_list: t.join()

def class_example():
    class SyncLock(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def run(self):
            self.job()

        def job(self):
            sync_locker.acquire()  
            print("worker: {}".format(self.name))
            time.sleep(0.1)
            sync_locker.release()

    sync_locker = threading.Lock()
    for i in range(10):  
        my_thread = SyncLock()
        my_thread.start()


if __name__ == '__main__':
    # function_example()    # non sequentially
    class_example()         # sequentially

   