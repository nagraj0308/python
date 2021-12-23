import math


def basics_of_python():
    # normal statements
    a = input("Enter value of a: ")
    b = input("Enter value of b: ")

    if a > b:
        print(a, " is greater")
    elif a == b:
        print("Both is Equal")
    else:
        print(b, " is greater")

    c = eval(input())
    print(type(c))

    e = 10
    f = 20
    e, f = f, e
    print(e, f)

    a = input().split(',', 3)
    print(a)


def all_math():
    print(".....................Math...................................................")
    print(math.ceil(23.34))
    print(math.ceil(-24.34))
    print(math.e)
    print(math.exp(7))
    print(math.e ** 7)
    print(math.floor(3.4444444444444))
    print(math.sqrt(2))
    print(math.log(5))
    print(math.log10(5))
    print(math.log(math.e))
    print(max(2, 4, 6, 7, 2, 4, 6, 7, 4, 100))
    print(min(2, 4, 6, 7, 2, 4, 6, 7, 4, 100))
    print(round(100.1223, 2))
    print(math.modf(10.0001))
    print(math.pow(2, 3))
    print(math.pi)
    print(math.degrees(4))
    print(math.radians(-180))

    a = 10
    print(a)
    del a
    # print(a)

    print("............................................................................")

    a = 7 - 4j
    b = a * 2
    print(b)

    print("............................................................................")
    print(ord("a"))
    print(hex(13))
    print(oct(10))
    print(bin(7))

    print("............................................................................")
    a = True
    b = False
    print(a and b)
    print(a or b)
    print(not b)


