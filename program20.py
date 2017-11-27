#single & multilevel inheritance
class NagRaj(object):
	
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def printname(self):
		print(self.name,self.age)
	
	def career(self): #abstration......
		raise "hello!! this isnot inplemented.."
class NagRajSon(NagRaj):
	
	def __init__(self,name,age,familycode):
		NagRaj. __init__(self,name,age)
		self.familycode=familycode
	
	def printname(self):#funoveride
		print(self.name,self.age,self.familycode)
	
	def career(self):
		print("Great Jobs!!")

class NagRajSonSon(NagRajSon):
	
	def __init__(self,name,age,familycode,sons):
		NagRajSon. __init__(self,name,age,familycode)
		self.sons=sons
	
	def printname(self):#fun reoverride
		print(self.name,self.age,self.familycode,self.sons)
	
		
	
o1=NagRaj("Nagendra","21")
o2=NagRajSon("A","1","NAGRAG")
o3=NagRajSonSon("B","2","NAGRAG",6)
o1.printname()
o2.printname()
o3.printname()
o2.career()
#o1.career()
o3.career()

