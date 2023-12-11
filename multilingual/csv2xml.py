fli = "strings.csv"
i = 0

# <string name="d8">8</string>
with open(fli, 'r') as file:
    for line in file:
        i = i + 1
        l = line.strip()
        items = l.split(',')
        str1 = "<string name=\"" + items[0] + "\">" + items[2] + "</string>"
        print(str1)
    print(i)
