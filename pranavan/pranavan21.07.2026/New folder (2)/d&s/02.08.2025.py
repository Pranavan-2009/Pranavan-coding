def printnumber(n):
    iteration=0
    print("The number enterd by user is ",n)
    iteration+=1
    print("Total iterations done by the code is ",iteration,"\n")

printnumber(5)
printnumber(10)
print("\n with any 'n' the time taken by our code won't change")

def onTime(n):
    iteration=0
    for i in range (1,n+1):
        iteration+=1
    print("when n is",n,"Iteratins =",iteration)

onTime(10)
onTime(20)
onTime(50)
print("\n with every 'n' the time taken and iterations will increase")

def ONSquareTime(n):
    iteration=0
    for i in range (0,n):
        for i in range (0,n):
            print("*",end="")
            iteration+=1
        print("")
    print("\nwhen n is",n,"Iteratins =",iteration,"\n")

ONSquareTime(4)
ONSquareTime(5)
ONSquareTime(6)
print("\n with every 'n' the time taken equals n^2")
print("O(n^2)")