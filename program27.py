def binfile():
	import pickle 
	file = open('file27.dat','wb') 
	while (True):
		x = input("Share Your Thoughts..\n") 
		pickle.dump(x,file) 
		ans = input('want to enter more data Y / N')
		if ans.upper()== 'N' : break
	file.close()
	file = open('file27.dat','rb')
	try :
		while( True) :
			y = pickle.load(file) 
			print(y) 
	except EOFError :
		pass
	file.close()


binfile()
