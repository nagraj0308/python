import math
import random

p, q = 619, 263
n = p * q

"""======================== FIEGE FIAT SHAMIR================================="""


def inverse(a):
    a = a % n
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return 1


k = 10
s = []
v = []
# Generating the Alice Private and Public Keys
for i in range(k):
    while (1):
        num = random.randint(0, n)
        if math.gcd(num, n) == 1:
            secret = num
            s.append(secret)
            break
    v.append(inverse(secret ** 2))
print(f"s = {s}")
print(f"v = {v}")
# Alice Generating the Witness
r = random.randint(10000, 20000)
x = r ** 2 % n
print(f"r = {r} , x = {x}")
# Bob sending a challenge vector
c = []
for i in range(k):
    c.append(random.randint(1, 10) % 2)
print(f"c = {c}")
# Alice sending response to Bob for the challenges
y = r
for i in range(k):
    y *= s[i] ** c[i]
y = y % n
print(f"y = {y}")
# Bob Verifying the Values
verifiable = y ** 210
for i in range(k):
    verifiable *= v[i] ** c[i]
verifiable = verifiable % n
print(f"verifiable = {verifiable}")
if verifiable == x:
    print("True")
else:
    print("False")

"""
# ===================== Guillou Quisquater protocol ========================#
print(f"R         X            E         C       Y       LHS      RHS    P/NP")
print("============================================================================================")
# Generating the Alice Private and Public Keys
phi = (p - 1) * (q - 1)
for i in range(10):
    r = random.randint(0, n)
    e = random.randint(2, phi)
    while (1):
        num = random.randint(0, n)
        if math.gcd(num, n) == 1:
            secret = num
            s = (secret)
            break
    v = (inverse(secret ** e, n))
    # Witness
    x = (r ** e) % n
    # challenge
    c = random.randint(1, e)
    # alice sending response
    y = (r * (s ** c)) % n
    # bob verifying
    verifiable = (y ** e) * (v ** c) % n

    if (verifiable == x):
        flag = "P"
    else:
        flag = "NP"
    print(f"{r}     {x}     {c}     {e}     {y}    {verifiable}     {x}     {flag}")
    
    """
