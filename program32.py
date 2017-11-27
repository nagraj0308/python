"""Program code for deletion of the line(s) having word ( passed as argument) is :"""

def fileDEL(word,fname):
	import os
	file=open(fname,"r")
	newfile=open("new.txt","w")

	while True:
		line = file.readline()
		if not line :
			break

		else :
			if word in line :
				pass
			else :
				print (line)
				newfile.write(line)
	file.close()
	newfile.close()
	os.remove(fname)
	os.rename("new.txt",fname)

fileDEL("void","file32.txt")
