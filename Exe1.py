newstring = input("Enter the string: ")
newfile = input("Enter the name of file: ")
file2 = open(newfile, 'w')
file2.write(newstring)
file2.close()
