import random

""" Fiat-Shamir Protocol """
p = 31
q = 29
n = p * q  # public

# alice end
s = random.randint(1, n - 1)  # keeps private key
v = (s * s) % n  # keeps public key
r = random.randint(1, n - 1)  # commitment
x = (r * r) % n  # witness
print("Alice : Sending x=", x, "to Bob as witness")

# bob end
c = random.randint(0, 1)
print("Bob   : Sending c=", c, "to Alice as challenge")

# alice end
y = (r * (s ** c)) % n
print("Alice : Sending y=", y, "to Bob as response")

# bob end
v1 = (y * y) % n
v2 = (x * (v ** c)) % n
if v1 == v2:
    print("Bob   : Probable")
else:
    print("Bob   : Improbable")





""" Feige-Fiat-Shamir Protocol """

k = 10
s = []
v = []
c = []
for i in range(k):
    r = random.randint(1, n)
    s.append(r)
    v.append((r * r) % n)
    c.append(random.randint(0, 1))

r = random.randint(1, n - 1)  # commitment
y1 = r
x = (r * r) % n  # witness
y2 = x
for i in range(k):
    y1 *= (s[i] ** c[i])
    y2 *= (v[i] ** c[i])

v1 = (y1 ** 2) % n
v2 = y2 % n

if v1 == v2:
    print("Bob   : Probable")
else:
    print("Bob   : Improbable")





""" Guillou-Quisquater Protocol """


def fi(a, b):
    return (a - 1) * (b - 1)


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def inverse(a):
    a = a % n
    for j in range(1, n):
        if (a * j) % n == 1:
            return j
    return 1


def bezout(a, b):
    oldB = b
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    if x < 0:
        x = x + oldB
    return x


p = 31
q = 29
f = fi(p, q)
e = random.randint(1, f)
while gcd(e, f) != 1:
    e = e + 1
s = bezout(e, f)
v = inverse(s ** e)
r = random.randint(1, n)
x = (r ** e) % n
c = random.randint(1, e)
y = (r * (s ** c)) % n
v1 = x
v2 = ((y ** e) * (v ** c)) % n
if v1 == v2:
    print("Bob   : Probable")
else:
    print("Bob   : Improbable")
