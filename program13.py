"""String methods & built in functions:
len() capitalize() find(sub[,start[, end]]) isalnum() isalpha()
isdigit() lower() islower() isupper() upper() lstrip()
rstrip() isspace() istitle() replace(old,new) join ()
swapcase() partition(sep) split([sep[,maxsplit]])"""

a="Nagendra0308"
b="ChaUdhary"
c="12222 hello tom nag anga nag nag nagg"

print(len(a))

print(b.capitalize())

print(a.find('en',1,7))

print(a.isalnum())
print(b.isalpha())
print(c.isdigit())

print(a.lower())
print(a)

print(a[1].isupper())

print(a.replace('a','A'))

print(a.isspace())

print(a.partition('a'))

print(a.split('ag',1))

print(b.lstrip())

print(b.rstrip())

print(a.join(b))

print(b.join(a))

print(a.swapcase())

print(c.count("nag"))
print(c.endswith("nagg"))



