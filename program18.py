class Health_profile:
	Weight=89
	Blood_group='B+'
	__BP=None       #private member
	def __init__(self):
		self.__BP = "Hidden attribute"
	def display_BP(self):
		print (self.__BP)


H =Health_profile()
#print(H.__BP)
H.display_BP()
