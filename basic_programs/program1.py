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
