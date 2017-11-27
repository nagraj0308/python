def fileoperation():
	import pickle
	l=[1,2,3,4,5,6]
	file=open("file26.dat","wb") # b in access modeisfor binary file
	pickle.dump(l,file)# writing content to binary file
	file.close()
fileoperation()
import pickle
file=open("file26.dat","rb")
print(pickle.load(file))
file.close()

