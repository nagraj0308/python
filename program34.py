# stack..........
s = []
c = "y"
while c == "y":
    print("1. PUSH")
    print("2. POP ")
    print("3. Display")
    choice = eval(input("Enter your choice: "))
    l = len(s)
    if choice == 1:
        a = input("Enter any number:")
        s.append(a)
    elif choice == 2:
        if l == 0:
            print("Stack Empty")
        else:
            print("Deleted element is : ", s.pop())
    elif choice == 3:
        for i in range(l - 1, -1, -1):
            print(s[i])
    else:
        print("Wrong Input")
    c = input("Do you want to continue or not? ")
