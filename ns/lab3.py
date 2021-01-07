""" Using Python find the points of an Elliptic Curve(y^2=x^3+ax+b)
 represented as Ep(a,b). Where p is the prime no. and
 a is the coefficients of x and  b is a constant."""
import math


def E(a, b, p):
    y_yy = []
    x_xx = []
    x_y = []
    for i in range(p):
        y_yy.append([i, (i * i) % p])
        x_xx.append([i, (i ** 3 + a * i + b) % p])
    for i in range(p):
        for j in range(p):
            if y_yy[i][1] == x_xx[j][1]:
                x_y.append([x_xx[j][0], y_yy[i][0]])

    print("Elliptic Curve : y^2=x^3 +", a, "x+", b)
    print("Points on Curve :")
    print(x_y)
    return x_y


a = 1
b = 6
p = 11
points_on_curve = E(a, b, p)

""" Case 1 : R = P + Q """


def mul_inverse(n):
    n = n % p
    for i in range(1, p):
        if (n * i) % p == 1:
            return i
    return 1


def slope(p1, p2):
    num = p2[1] - p1[1]
    den = p2[0] - p1[0]
    if den != 1:
        den = mul_inverse(den)
        return (num * den) % p
    else:
        return num


def new_point():
    p1 = points_on_curve[0]
    p2 = points_on_curve[math.floor(len(points_on_curve) / 2)]
    s = slope(p1, p2)
    x3 = (s ** 2 - p2[0] - p1[0]) % p
    y3 = (s * (p1[0] - x3) - p1[1]) % p
    return [x3, y3]


print("New point on curve : ", new_point())

""" Case 2 : R = P + P """


def slope2(p1):
    num = 3 * (p1[0] ** 2) + a
    den = 2 * p1[1]
    if den != 1:
        den = mul_inverse(den)
        return (num * den) % p
    else:
        return num


def new_point2():
    p1 = points_on_curve[0]
    s = slope2(p1)
    x3 = (s ** 2 - p1[0] - p1[0]) % p
    y3 = (s * (p1[0] - x3) - p1[1]) % p
    return [x3, y3]


print("New point on curve : ", new_point2())
