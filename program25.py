def fileHandling():
	file = open("file25.txt","w+")
	while (True):
		line =input("enter sentence :")
		file.write(line)
		choice =input("want to enter more data in file Y/N")
		if (choice.upper() == 'N') : break
	file.seek(0)
	lines = file.readlines()
	file.close()
	for l in lines:
		print (l)

fileHandling()
