import math
import random

a = 1
b = 6
p = 11
coordinates = []


def f(s):
    s2 = 2
    return s2


y = []
x = []
for i in range(p):
    num = f(i)
    if num != -1:
        x.append(i)
        y.append(num)
for i in range(len(x)):
    if y[i] >= 0:
        coordinates.append([x[i], y[i]])
        coordinates.append([x[i], p - y[i]])

"""**Printing the coordinates**"""

for item in coordinates:
    print(item)

"""**Case 1 : R = P + Q**"""


def mulInverse(n, p):
    n = n % p
    for x in range(1, p):
        if ((n * x) % p == 1):
            return x
    return 1


def slope(x1, y1, x2, y2):
    num = y2 - y1
    den = x2 - x1
    if den != 1:
        # find inverse of it in mod p
        den = mulInverse(den, p)
        return (num * den) % p
    else:
        return num


def add_coordinates(index1, index2):
    x1 = coordinates[index1][0]
    x2 = coordinates[index2][0]
    y1 = coordinates[index1][1]
    y2 = coordinates[index2][1]
    new_coordinate = []
    s = slope(x1, y1, x2, y2)
    x3 = (s ** 2 - x2 - x1) % p
    y3 = (s * (x1 - x3) - y1) % p
    new_coordinate.append(x3)
    new_coordinate.append(y3)
    return new_coordinate


# Index of the coordinates starts from 0
index1 = int(input("Enter P coordinate index "))
index2 = int(input("Enter Q coordinate index "))
add_coordinates(index1, index2)

"""**Case 2 : R = P + P**"""


def slope_2(x1, y1, scalar):
    num = 3 * x1 ** 2 + scalar
    den = 2 * y1
    if (den != 1):
        den = mulInverse(den, p)
        return (num * den) % p
    else:
        return num


def twice_coordinate(index, scalar):
    new_coordinate = []
    x1 = coordinates[index][0]
    y1 = coordinates[index][1]
    s = slope_2(x1, y1, scalar)
    x3 = (s ** 2 - x1 - x1) % p
    y3 = (s * (x1 - x3) - y1) % p
    new_coordinate.append(x3)
    new_coordinate.append(y3)
    return new_coordinate


def find_index(coor):
    for i in range(len(coordinates)):
        if (coordinates[i] == coor):
            return i


def case2(index, scalar):
    new_coor = twice_coordinate(index, 2)
    old_index = index
    new_index = find_index(new_coor)
    for i in range(scalar - 2):
        if (old_index == new_index):
            # again apply case 2 i.e P+P
            new_coor = twice_coordinate(new_index, 2)
        else:
            # apply case 1 i.e P + Q
            new_coor = add_coordinates(new_index, old_index)
        old_index = new_index
        new_index = find_index(new_coor)
    return new_coor


index = int(input("Enter P coordinate index "))
scalar = int(input("Enter the Scalar "))
coor = case2(index, scalar)
print(coor)
