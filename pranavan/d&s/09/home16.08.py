

numberLargest = int(input("Enter Largest number: "))
numberSmallst = int(input("Enter Smallst number: "))

while(numberSmallst):
    numberStore = numberSmallst
    numberSmallst = numberLargest % numberSmallst
    numberLargest = numberStore

print("LCM is:", numberSmallst)