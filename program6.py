a=[1,2,'hello']
print(a,len(a),type(a))
for i in a:
	print(i)


print(a[2])
print(a[0:2])

# List Methods:
#    append() extend () pop() del() remove()
#    insert() sort() reverse() len()

a.append(100)
print(a)

b=[20,300]
a.extend(b)
print(a)

a.append(b)
print(a)

a.pop(2) #pop works by using index
print(a)

a.append(b)
print(a)

a.pop(6) #pop works by using index
print(a)

del(a[2])#del works by using index
print(a)

a.remove(20)
print(a)

a.remove(b)
print(a)

a.insert(2,"insert")
print(a)

a.reverse()
print(a)

#a.sort()
#print(a)

print(a+a)
print(a*2)
#print(a&a)

a=[1,2,3,4,5,5,6,4,5,1,68,6,545,7,8,89,9]
print(max(a))
print(a.count(5))


""" list comprehension"""

"""syntax:new_list=[expression(i) for i in old_list if condition]"""

x=[i*i for i in range(10)]
print(x)

x=[i*i for i in range(10) if i%2==0]
print(x)

words=["ABC","DEF","GHI","JKL"]
print(words)
words2=[i[0] for i in words]
print(words2)



