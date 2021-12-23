import sys


def all_memory():
    reference_cycle()


# GarbageCollector:-1. Reference Counting @.Automatic Garbage Collector calling..
def reference_cycle():
    x = []
    x.append(x)  # cyclic so increasing in the reference of x variable.


def all_system():
    # command line argument.....
    """sys.argv is a list in python ,which contains command line arguments passed to script"""
    print("The namer of the script:", sys.argv[0])
    print("The number of the arguments are:", len(sys.argv))
    print("The arguments are:", str(sys.argv))
