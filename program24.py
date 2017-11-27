s = ['this is 1stline','this is 2nd line']
file1=open("file24.txt","w")
file1.writelines(s)
file1.close()

file=open("file24.txt","r")
print (file.read())
file.close()

"""writelines() does not add any EOL
character to the end of string. You have to do itby adding \n"""

s = ['this is 1stline\n','this is 2nd line\n']
file1=open("file24.txt","w")
file1.writelines(s)
file1.close()

file=open("file24.txt","r")
print (file.read())
file.seek(5,0) #seek is used to send cursor at specific point
print(file.read(5))#now file read next5 byte from 5

print(file.tell())#it should be 5+5=10

file.close()

""" Value  reference point
	0 beginning of the file
        1 current position of file
	2 end of file"""
