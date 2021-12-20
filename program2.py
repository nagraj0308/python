def all_loops():
    for i in range(1, 10, 2):
        print(i, "st line")

    n = 4
    for i in range(0, n):
        print(i)

    t = ("geeks", "for", "geeks")
    for i in t:
        print(i, end=' ')

    j = 0
    while j < 10:
        print("we are in", j, "st Line of while loop")
        j = j + 1
