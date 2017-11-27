"""__dict__ : It gives the dictionary containing the class's namespace.
   __doc__ : It returns the class's documentation string(also called docstring) and if no docstring is
		defined for a class this built in attribute returns None
   __name__: It gives the class name.
   __module__: It specifies the module name in which the class is defined. This attribute is called
                 "__main__" in interactive mode.
   __bases__ : It gives a possibly empty tuple containing the base classes 
   del(o1)  
   str()"""

class NagRaj:
	"you are fortunate that you know NagRaj"
	mobile=7060196036
	age=22
	def __init__(self,mobile,age):
		self.age=age
		self.mobile=mobile
	def saluteNagraj(self):
		print("NagRaj!! We salute You.")
	def __str__(self):
		return( "Hello, How are you?")

print(NagRaj.__doc__)
print(NagRaj.__name__)
print(NagRaj.__module__)
print(NagRaj.__bases__)
print(NagRaj.__dict__)

o=NagRaj(23,34)
print(o)
del(o)



	

	

