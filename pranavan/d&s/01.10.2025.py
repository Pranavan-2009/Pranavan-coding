import math;
def printPowerSet(set,Setsize):

    powersetsize = (int)(math.pow(2,Setsize));
    outer = 0;
    inner = 0;

    for outer in range(0,powersetsize):
        for inner in range(0,Setsize):

            if((outer & (1 << inner)) > 0):
                print(set[inner],end = "")
        print("")

size = int(input("Enter array size: "))
set = []
for i in range(0,size):
    n = int(input("Enter element: "))
    set.append(n)

printPowerSet(set,size)

def totalflips(number1,number2):
    flips = 0


    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 1)
        if(t1 != t2):
            flips += 1

            number1>>=1
            number2>>=1

    return flips
    
number1 = int(input("Enter number : "))
number2 = int(input("Enter number : "))

print("\nNumber of flips needed :",totalflips(number1,number2))

