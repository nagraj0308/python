def all_oops():
    o1 = NagRaj("NAG-RAJ", "21")
    o2 = NagRajSon("NAG-RAJ-SON", "1", "NAG-RAJ")
    o3 = NagRajSonSon("NAG-RAJ-GRAND-SON", "2", "NAG-RAJ", 6)
    o1.printname()
    o2.printname()
    o3.printname()
    o2.career()
    # o1.career()
    o3.career()

    # multiple inheritance
    o = NagRajGrandSon("Nagendra", "21", "NAGRAJ")
    o1 = NagRajSon1("A", "1")
    o2 = NagRajSon2("B", "5")
    o3 = NagRajSon3("C", "9", )
    o.printname()
    o1.printname()
    o2.printname()
    o3.printname()


# single & multilevel inheritance
class NagRaj(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)

    def career(self):  # abstraction......
        raise "hello!! this is not implemented.."


class NagRajSon(NagRaj):

    def __init__(self, name, age, family_code):
        NagRaj.__init__(self, name, age)
        self.family_code = family_code

    def printname(self):  # override
        print(self.name, self.age, self.family_code)

    def career(self):
        print("Great Jobs!!")


class NagRajSonSon(NagRajSon):

    def __init__(self, name, age, family_code, sons):
        NagRajSon.__init__(self, name, age, family_code)
        self.sons = sons

    def printname(self):  # fun override
        print(self.name, self.age, self.family_code, self.sons)


# multiple inheritance
class NagRajSon1(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)


class NagRajSon2(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):  # override
        print(self.name, self.age)


class NagRajSon3(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):  # override
        print(self.name, self.age)


class NagRajGrandSon(NagRajSon1, NagRajSon2, NagRajSon3):

    def __init__(self, name, age, family_code):
        NagRajSon1.__init__(self, name, age)
        NagRajSon2.__init__(self, name, age)
        NagRajSon3.__init__(self, name, age)
        self.family_code = family_code

    def printname1(self):  # override
        print(self.name, self.age, self.family_code)
