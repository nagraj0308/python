import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime())

bday=(1992,8,3,17,18,19,0,0,0)
print(time.mktime(bday))
print(time.localtime(time.mktime(bday)))

time.sleep(8)
print("Hello NagRaj")
