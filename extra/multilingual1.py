import pandas as pd

# Specify the path to your XML file
fli = "strings.xml"
flo = "strings.csv"
i = 0
j = 0
datao = []

with open(fli, 'r') as file:
    for line in file:
        i = i + 1
        l = line.strip()
        item_id = l.split('"')[1]
        t1 = l.split('"')[2].split("</string>")[0][1:]
        print(item_id, t1)
        j = j + len(t1.split(" "))
        datao.append([item_id, t1])
    print(i, j)
    print(datao)
    f = pd.DataFrame(datao)
    f.to_csv(flo, index=False)
