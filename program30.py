#Program Code for creating a copy of existing file:

ifile = open("file30r.txt","r")
ofile = open("file30w.txt","a")
l = ifile.readline()
while l:
	ofile.write(l)
	l = ifile.readline()
ifile.close()
ofile.close()
