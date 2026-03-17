file_read = open('./pranavan.txt','r')
print(file_read.read())
file_read.close()

file_read = open('./pranavan.txt','r')
print("\n Read in parts \n")
print(file_read.read(8))
file_read.close()

file = open('./pranavan.txt','a')
file.write("Hi! I am penguin. I am 1  yr old")
file_read.close()

file_read = open('./pranavan.txt','r')
print("Reading first lines.....")
print(file_read.readline())
file.close()

file_read = open('./pranavan.txt','r')
print("Reading multiple lines.....")
print(file_read.readline())
print(file_read.readline())
print(file_read.readline())
file.close()

file_read = open('./pranavan.txt','r')
print("Looping through the lines....")
for line in file_read:
    print(line)
file_read.close()