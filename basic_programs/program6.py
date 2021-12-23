def variable_length_arg():
    fun1(3, 5)
    fun1(4, 5, 6, 7)
    fun1(1, 2, 3, 5, 6)
    fun2(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
    fun2(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


def fun1(*num):
    s = 0
    for n in num:
        s = s + n
    print("Sum:", s)


def fun2(**data):
    print("\nData type of argument:", type(data))
    for key, value in data.items():
        print("{} is {}".format(key, value))
