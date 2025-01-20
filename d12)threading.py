"""
def first():
    for i in range(5):
        print("hi")
        
def sec():
    for i in range(5):
        print("bye")

first()
sec()
"""

"""
import threading
import time

def print_cube(num):
    # for i in range(num):
    #     time.sleep(4)
        print("Cube: {} ".format(num*num*num))

def print_square(num):
    # for i in range(num):
    #     time.sleep(2)
        print("Square: {} ".format(num*num))

if __name__ == "__main__":
    # creating thread - tuple datatypes hence ',' should be given in args
    t1 = threading.Thread(target=print_square, args=(5,))
    t2 = threading.Thread(target=print_cube, args=(5,))
    
    t1.start()
    # t1.join()
    t2.start()
    # t2.join()
"""
"""
import threading
import os

def task1():
    print("\nTask 1 assigned to thread: {}".format(threading.current_thread().name))
    print("\nID of process running task 1 : {}".format(os.getpid()))


def task2():
    print("\nTask 2 assigned to thread: {}".format(threading.current_thread().name))
    print("\nID of process running task 2 : {} ".format(os.getpid()))


if __name__ == "__main__":
    print("\nID of process running main program : {}".format(os.getpid()))
    print("\nMain thread name : {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name="Thread1")
    t2 = threading.Thread(target=task2, name="Thread2")

    t1.start()
    # t1.join()
    t2.start()
    # t2.join()
"""
"""
import threading
import time


def sleepy(secs):
    print("\nStarting to sleep inside {}".format(time.asctime()))
    time.sleep(secs)
    print("\nWoke up inside {} ".format(time.asctime()))


if __name__ == "__main__":
    x = threading.Thread(target=sleepy, args=(10,))
    x.start()
    x.join()
    print("\nActive threads: ", threading.active_count())
    time.sleep(20)
    print(time.asctime())
    print("Code end")
"""