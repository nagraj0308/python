import re

k = re.match("([a-z]+[0-7])+", 'br11')
print(k.groups())

print("................................................................")
name = ["A1B1", "djdd", "B1C1", "C2H2", "Adoi", "1A4V"]
for element in name:
    m = re.match("(^[A-B]\d[A-B]\d)", element)
    if m:
        print(m.groups())
