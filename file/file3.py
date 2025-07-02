file_read = open('file.txt','r')
print(file_read.read())
file_read.close()

file_write = open('file.txt','r')
print("\n Read in parts \n")
print(file_read.read(8))
file_read.close()

file = open('file.txt','a')
file.write("Hi! I am penguin. I am 1  yr old")
file_read.close()