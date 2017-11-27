class Health_profile:
	weight=0
	blood_group='B+'
	def __init__(self,weight,blood_group):
		self.weight=weight
		self.blood_group=blood_group
	def display(self):
		print( " Weight :" , self.weight)
		print ("Blood Group : " , self.blood_group)

H2=Health_profile(61 ,'A+')
H2.display()
