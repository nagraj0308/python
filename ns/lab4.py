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

""" Guillou-Quisquater Protocol """
