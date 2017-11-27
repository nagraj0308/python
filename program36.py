"""S.	 No. Error type Description
1. IOError 		is raised when I/O operator fails. Eg. File not found, disk full
2. EOFError 		is raised when, one of the file method i.e. read(), readline() or
				readlines(), try to read beyond the file.
3. ZeroDivisionError    is raised when, in division operation, denominator is zero
4. ImportError 		is raised when import statement fails to find the module definition or
				file name
5. IndexError	        is raised when in a sequence - index/subscript is out of range.
6. NameError 		is raised when a local or global name is not found
7. IndentationError     is raised for incorrect indentation
8. TypeError 		is raised when we try to perform an operation on incorrect type of
				value.
9. ValueError 		is raised when a built in function/method receives an argument of
				correct type but with inappropriate value."""



"""l = [1,2,3]
i = 5
if i > len(l):
	raise IndexError
	
else:
	print (l[i])"""
	

print("..............................................................................")




def fun(x,y):
	try:
		print("Before expression")
		c=x/y
		print("After expression")
		#c=int(x)//int(y)
	except IOError:
		print("is IOError")
	except EOFError:
		print("is EOFError")
	except TypeError:
		print("is TypeError")
	except ImportError:
		print("is ImportError")
	except NameError:
		print("is NameError")
	except IndentationError:
		print("is IndentationError")
	except ValueError:
		print("is ValueError")
	except ZeroDivisionError:
		print("is Zero Divison")
	else:
		print(c)

	finally:
		print("Final Statement")

fun("p",3)
fun(2,3)
fun(2,0)




