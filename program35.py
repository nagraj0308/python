# Queue
a = []
c = 'y'
while c == 'y':
    print("1. INSERT")
    print("2. DELETE ")
    print("3. Display")
    choice = eval(input("enter your choice "))
    l = len(a)
    if choice == 1:
        b = input("enter new number ")
        a.append(b)
    elif choice == 2:
        if l == 0:
            print("Queue Empty")
        else:
            print("deleted element is:", a[0])
            del a[0]
    elif choice == 3:
        for i in range(0, l):
            print(a[i])
    else:
        print("wrong input")
    c = input("do you want to continue or not ")
