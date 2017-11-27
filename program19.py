#static method

class SM:
	@staticmethod
	def square(x):
		SM.result= x*x

SM.square(5)               #static method dont requred object to call
print(SM.result)

SM().square(5)
print(SM.result)

T1=SM()
T1.square(5)
print(T1.result)


#GarbageCollector:-1.Refrence Counting @.Automatic Garbage Collector calling..

def reference_cycle():
	x=[ ]
	x.append(x)  #cyclic so increasing in the refernce of xvariable..
reference_cycle()
