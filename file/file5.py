with open('./pranavan.txt','a') as file:
  file.write("Hi! I am penguin. I am 1  yr old")
file.close()

with open('./pranavan.txt','r') as file:
    data = file.readlines()
    print("Words in this file are.....")
    for line in data:
        word = line.split()
        print(word)
file.close()