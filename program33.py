import os
import sys
import pickle

def bfileCreate(fname):
	l = []
	sd = {1000:"['anuj',12,450]"}
	with open(fname,'wb') as ofile :
		while True :
			pickle.dump(sd,ofile)
			ans = input("want to enter more data Y / N")
			if ans.upper() == 'N' : break
			x = int(input("enter admission number of student"))
			l = input("enter name class and marks of student enclosed in []")
			sd[x] = l
	ofile.close()


def bfileDisplay(fname):
	if not os.path.isfile(fname) :
		print ("file does not exist")
	else:
		ifile = open(fname,'rb')
	try :
		while True:
			sd = {}
			sd= pickle.load(ifile)
			print( sd)
	except EOFError:
		pass
	ifile.close()



bfileCreate("file33.dat")

bfileDisplay("file33.dat")

