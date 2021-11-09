inputfile = input("Enter the name of file: ")
file = open(inputfile,"r")
print(file.read())
file.close()