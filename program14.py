class c14:
	a="NULL"
	b="NUll"
	k=0
	def __init__(self,u=10,v=20):
		c14.a=u
		c14.b=v
	
	def add(self,a,b):
		return(a+b)

	def display(self,a):
		print(a)


p=c14(5,6)
c=p.add(2,3)
p.display(c)

print(p.b)
p.b=100

"""self refers to the newly created object or the instance whose method was called."""

"""To understand why you don't need to give any value for self during the method call, consider an example.
Say you have a class called My_Photo and an instance of this class called My_Object. When you call a
method of this object as My_Object.method(arg1, arg2), this is automatically converted by Python into
My_Photo.method (My_Object, arg1, arg2)."""

print(vars(p))#this shows instance attributes in for of dictonary.
print(dir(p))#this shows class attributes...
