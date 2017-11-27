#multiple inheritance
class NagRajSon1(object):
	
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def printname(self):
		print(self.name,self.age)
	
	
class NagRajSon2(object):
	
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
	def printname(self):#funoveride
		print(self.name,self.age)
	
	
class NagRajSon3(object):
	
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
	def printname(self):#funoveride
		print(self.name,self.age)
	


class NagRaj(NagRajSon1,NagRajSon2,NagRajSon3):
	
	def __init__(self,name,age,familycode):
		NagRajSon1. __init__(self,name,age)
		NagRajSon2. __init__(self,name,age)
		NagRajSon3. __init__(self,name,age)
		self.familycode=familycode
	
	def printname1(self):#funoveride
		print(self.name,self.age,self.familycode)
	
	



		
o=NagRaj("Nagendra","21","NAGRAJ")	
o1=NagRajSon1("A","1")
o2=NagRajSon2("B","5")
o3=NagRajSon3("C","9",)
o.printname()
o1.printname()
o2.printname()
o3.printname()



