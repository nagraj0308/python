#Adding run time method

from types import MethodType  #type and Method are built in

class c(object):
	a=20



def play(self):
	print("Sports Keeps You Live!!")

h=c()
h.p=MethodType(play,h)
h.p()

#In above only object h will have play method..

print(getattr(h,"a",10))
print(hasattr(h,"a"))
setattr(h,"b",140)
print(getattr(h,"b",10))
delattr(h,"b")
print(hasattr(h,"b"))




