import threading
import os


def all_thread():
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")

    # p2
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t3 = threading.Thread(target=task1, name='t3')
    t4 = threading.Thread(target=task2, name='t4')

    # starting threads
    t3.start()
    t4.start()

    # wait until all threads finish
    t3.join()
    t4.join()


def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


def print_square(num):
    print("Square: {}".format(num * num))


def print_cube(num):
    print("Cube: {}".format(num * num * num))
