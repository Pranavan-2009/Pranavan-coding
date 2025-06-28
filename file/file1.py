file_read = open('file.txt','r')
print("file in read mode -")
print(file_read.read())
file_read.close()

file_write = open('file.txt','w')
file_write.write("file in write mode ....")
file_write.write("Hi! I am Penguin. I am 1yr.old ")
file_write.close()

file_write = open('file.txt','a')
file_write.write("\nfile in append mode ....")
file_write.write("Hi! I am Penguin. I am 1yr.old ")
file_write.close()
