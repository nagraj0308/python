import os

file=open("data_files/file28a.txt", "r")

print(os.path.abspath("data_files/file28a.txt"))#will give us the complete path name of the data file.


print(os.path.isfile("data_files/file28a.txt"))

print(file.closed,file.mode,file.name)

print(os.getcwd())#to know the name of current working directory

