import math;
def printPowerSet(set,Setsize):

    powersetsize = (int)(math.pow(2,Setsize));
    outer = 0;
    inner = 0;

    for outer in range(0,powersetsize):
        subset = []
        for inner in range(0,Setsize):

            if((outer & (1 << inner)) > 0):
                subset.append(set[inner])
        print(''.join(subset))

size = int(input("Enter array size: "))
set = []
for i in range(0,size):
    n = input("Enter element: ")
    set.append(n)

printPowerSet(set,size)

