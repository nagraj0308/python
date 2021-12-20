file=open("data_files/file23.txt", "r")
file1=open("data_files/file23.txt", "a")
print(file1.write(file.read()))


