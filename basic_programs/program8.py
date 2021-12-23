def all_class():
    m = Motor('BAGGED', 5, 6)
    m.show_owner()
    m.show_code()
    m.show_class_variables()
    print(vars(m))  # this shows instance attributes in form of dictionary.
    print(vars(Motor))  # this shows class attributes in form of dictionary.
    print(dir(m))  # this shows class attributes...

    print(Motor.__doc__)
    print(Motor.__name__)
    print(Motor.__module__)
    print(Motor.__bases__)
    print(Motor.__dict__)
    print(m.__str__())
    print(m.__repr__())

    print(m)
    del m

    print("----------------SM---------------")
    SM.square(2)  # static method don't required object to call
    print(SM.cube(4))
    print(SM.result)

    SM().square(5)
    print(SM.result)

    T1 = SM()
    T1.square(3)
    print(T1.result)


class Motor:
    k = 0

    def __init__(self, code, u=10, v=20):
        self.wheel = u
        self.light = v
        self._owner = "owner"  # we "_"before variable to hint that this variable is private it's just a notation
        self.__code = code

    def show_owner(self):
        print('Owner of motor is : ', self._owner)

    def show_code(self):
        print('Owner of motor is : ', self.__code)

    def show_class_variables(self):
        print('k : ', self.k)


# static method
class SM:
    @staticmethod
    def square(x):
        SM.result = x * x

    @staticmethod
    def cube(x):
        return x * x * x


""" 
Single Leading Underscore(_var): Naming convention indicating a name is meant for internal use. Generally not enforced 
  by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only.
Single Trailing Underscore(var_): Used by convention to avoid naming conflicts with Python keywords.
Double Leading Underscore(__var): Triggers name mangling when used in a class context.Enforced by Python interpreter.
Double Leading and Trailing Underscore(__var__): Indicates special methods defined by the Python language. Avoid this 
    naming scheme for your own attributes.
Single Underscore(_): Sometimes used as a name for temporary or insignificant variables (“don’t care”). 
    Also: The result of the last expression in a Python

"""

"""__dict__ : It gives the dictionary containing the class's namespace.
   __doc__ : It returns the class's documentation string(also called docstring) and if no docstring is
        defined for a class this built in attribute returns None
   __name__: It gives the class name.
   __module__: It specifies the module name in which the class is defined. This attribute is called
                 "__main__" in interactive mode.
   __bases__ : It gives a possibly empty tuple containing the base classes
   del(o1)
   str()

"""
