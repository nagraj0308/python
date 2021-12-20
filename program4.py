def all_tuple():
    # Tuple functions:
    # cmp( ) len( ) max( ) min( ) tuple( )
    a = tuple()
    print(type(a), a)
    a = (1, 4)
    print(a)

    t = (2, 4, 5, 6, 'Nagraj')
    print(t)
    print(t[1:3])
    print(t[0])
    print(4 in t, len(t))
    print(t + t)
    print(t * 3)
    p, q, r, s, u = t  # unpacking of tuple
    print(p, q, s)

    sett = {1, 2, '4', 'nagraj'}
    print(sett, type(sett))
    tu = tuple(sett)
    print(tu, type(tu))
    li = [1, 2, 3, "Nagraj"]
    print(li, type(li))
    tu2 = tuple(li)
    print(tu2, type(tu2))

    t2 = (8, 4, 5)
    print(min(t2))
    print(max(t2))
