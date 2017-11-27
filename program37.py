"""The primary difference between generator and normal function is that generator will yield a value instead
of returning a value."""
def testGenerator():
	yield 1
	yield 2
	yield 3

g=testGenerator()
print(next(g))
print(next(g))
print(next(g))

def counter (n):
	i = 1
	while (i<=n):
		yield i
		i+=1
g= counter (3)
print(next(g))
print(next(g))
print(next(g))
