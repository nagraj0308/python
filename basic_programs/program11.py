def all_generator():
    g = test_generator()
    c = counter(3)

    print(next(g))
    print(next(g))
    print(next(c))
    print(next(g))
    print(next(c))
    print(next(c))


"""The primary difference between generator and normal function is that generator 
    will yield a value instead of returning a value."""


def test_generator():
    yield "hi"
    yield "NagRaj"
    yield "How are you.."


def counter(n):
    i = 1
    while i <= n:
        yield i
        i += 1
