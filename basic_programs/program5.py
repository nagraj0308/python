def all_dict():
    a = dict()

    print(a)
    d = {"Ek": 1, "Do": 2}
    print(d)

    print(d["Ek"], d['Do'])

    c = d.get("Ek")
    print(c)
    c = d.get("Ek", "2")
    print(c)

    print(d.keys())

    print(d.items())

    print(d.values())

    d.update({'Teen': 3})
    print(d)

    print(type(d), len(d))

    li = list(d.values())
    print(li)

    li = list(d.keys())
    print(li)

    print(d.clear())
