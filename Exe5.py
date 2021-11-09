import random 
randomlist = [random.randrange(-1000,1001) for i in range (0,1000)]
inputfile = input("Enter the name of file: ")
#Open file to write
file1 = open(inputfile,"w")
for i in range(0,100):
    for j in range(0,10):
        if j== 9:
            file1.write(str(randomlist[i*10 + j]))
        else:
            file1.write(str(randomlist[i*10 + j]) + ",")
    file1.write("\n")
file1.close()

#Open file to read
file2 = open(inputfile,"r")
valueofline= file2.readline()
while valueofline != "":
    newlist = valueofline.split(",")
    newstring = "\t".join(newlist)
    print(newstring)
    valueofline= file2.readline()
file2.close()

