file_read = open('file.txt','r')
counter = 0

content = file_read.read()

coList = content.split("\n")

for i in coList:
    if i:
        counter  += 1
        print("This is the number of line in the file ")
        print(counter)