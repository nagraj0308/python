""" Using Python find the points of an Elliptic Curve(y^2=x^3+ax+b)
 represented as Ep(a,b). Where p is the prime no. and
 a is the coefficients of x and  b is a constant."""


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


E(1, 6, 11)
E(1, 10, 17)
