def checkIfsame(number1, number2):
    if  ((number1^number2)!=0):
        print("Numbers are not equal")
    else:
        print("Both Numbers are equal")

number1 = int(input("Enter first number to compare: "))
number2 = int(input("Enter second number to compare: "))

checkIfsame(number1,number2)

def oddoccurring(arr):

    res = 0

    for element in arr:
        res = res ^ element

    return res
arr = []
n = int(input("Enter array size: "))
while(n):
    num = int(input("Enter number: "))
    arr.append(num)
    n-=1

print("\n\nodd occurring number is: ",oddoccurring(arr))
