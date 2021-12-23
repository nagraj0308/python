def all_string():
    a = "Nagendra"
    b = "     Chaudhary"
    print(a + b)
    print(a * 3)
    print("a" in a)
    print("o" not in b)
    print("au" not in b)
    for i in range(1, 5, 1):
        print(a[i])

    print(a[2:8])
    print(a[-2:])

    a = "Nagendra0308"
    b = "ChaUdhary"
    c = "12222 hello tom nag anga nag nag nagg"

    print(b.capitalize())
    print(a.find('en', 1, 7))
    print(a.isalnum())
    print(b.isalpha())
    print(c.isdigit())
    print(a.lower())
    print(a)
    print("----------------------------------------")
    print(a[1].isupper())
    print(a.replace('a', 'A'))
    print(a.isspace())

    print(a.partition('a'))

    print(a.split('ag', 1))

    print(b.lstrip())

    print(b.rstrip())

    print(a.join(b))

    print(b.join(a))

    print(a.swapcase())

    print(c.count("nag"))
    print(c.endswith("nagg"))
