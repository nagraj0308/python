with open("data_files/file31.txt", "r") as dfile:
	l=dfile.readlines()
dfile.close()

print(l)
del l[1]
print(l)



file=open('data_files/file31.txt', 'w')
file.writelines(l)
file.close()


