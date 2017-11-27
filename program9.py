def main():
	print("We are in main")
	print(fun1(5))
def fun1(a):
	a=a+5
	return(a)
main()




def fun(*tuple):
	for i in tuple:
		print(i)

fun(2,3,45,5)
fun(2,3)
