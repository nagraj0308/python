#hierarchical inheritance
class NagRaj(object):
	
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def printname(self):
		print(self.name,self.age)
	
	
class NagRajSon1(NagRaj):
	
	def __init__(self,name,age,familycode):
		NagRaj. __init__(self,name,age)
		self.familycode=familycode
	
	def printname(self):#funoveride
		print(self.name,self.age,self.familycode)
	
	
class NagRajSon2(NagRaj):
	
	def __init__(self,name,age,familycode):
		NagRaj. __init__(self,name,age)
		self.familycode=familycode
	
	def printname(self):#funoveride
		print(self.name,self.age,self.familycode)
	


class NagRajSon3(NagRaj):
	
	def __init__(self,name,age,familycode):
		NagRaj. __init__(self,name,age)
		self.familycode=familycode
	
	def printname(self):#funoveride
		print(self.name,self.age,self.familycode)
	
	



		
o=NagRaj("Nagendra","21")	
o1=NagRajSon1("A","1","NAGRAJ")
o2=NagRajSon2("B","5","NAGRAJ")
o3=NagRajSon3("C","9","NAGRAJ")
o.printname()
o1.printname()
o2.printname()
o3.printname()


