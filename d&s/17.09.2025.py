def numberOfbits(n):
    ones = 0
    zeros = 0

    while (n):
        if(n&1==1):
            ones += 1
        else:
            zeros += 1
        n = n >> 1
    print("\n\nOnes = ", ones,"\nZeros ", zeros)

number = int(input("Enter a number: "))
numberOfbits(number)

def setOrNot(number,n):
    if number & (1<< (n - 1)):
        print("\nSet")
    else:
        print("\nNot Set")

number = int(input("Enter a number: "))
n = int(input("Enter the bit position to check: "))
setOrNot(number,n)