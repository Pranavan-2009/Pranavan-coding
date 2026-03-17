num=23
for i in range (13):
    print("23 x",i,"=",num*i)

n=int(input("enter number of rows you want ??"))
for i in range (1,n+1):
    for i in range (i):
        print("*",end="")
    print()

total_sum=sum(range(1,11))
print(f"the sum of the first ten natural numbers is{total_sum}")

num=int(input("enter a number"))
if num>1:
    for i in range (2,int (num**0.5+1)):
        if num%i==0:
         print(f"{num} is not a prime number")

    else:
     print(f"{num} is a prime number")
else:
    print(f"{num} is not prime number")