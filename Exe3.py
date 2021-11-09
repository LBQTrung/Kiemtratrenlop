inputfile = input("Enter the name of file: ")
newstring = input("Enter the string: ")
newstring =", " + newstring 
file = open(inputfile,"a")
file = file.write(newstring)
file.close()
