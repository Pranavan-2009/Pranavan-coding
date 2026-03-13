import os
print("Checking if my file exists or not.....")
if os.path.exists("pranavan.txt"):
    os.remove("pranavan.txt")
else:
    print("The file dose not exist")