"""The standard streams available in python are
1-Standard input stream

2-Standard output stream and

3-Standard error stream
These standard streams are nothing but file objects, which get automatically connected to your program's
standard device(s), when you start python. In order to work with standard I/O stream, we need to import
sys module. Methods which are available for I/O operations in it are

1-read() for reading a byte at a time from keyboard
2-write() for writing data on terminal i.e. monitor"""

#Example..
import sys
print("Enter your name..: ")

	c=sys.stdin.read()
	if (c=='a'):
		break
	name=name+c
	sys.stdout.write("Your Name is: ",name)



#same can be done using high level methods also
name = input('Enter your name :')
print ('your name is ',name)
