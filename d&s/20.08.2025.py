from math import sqrt

number = int(input("Enter your number:"))
print("\n")

if number > 1:
    for i in range(2,int(sqrt(number)) + 1):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number,"is not a prime number")

def Sieve0fEratosthenes(num):
    prime = [True for i in range(num + 1)]

    p = 2
    while (p*p <= num):

        if(prime[p] == True):
            for i in range(p*p,num+1,p):
                prime[i] = False

        p+=1

    for p in range(2,num+1):
        if prime[p]:
            print(p) 

num = int(input())
print("Folowing are the prime numbers smalller")
print("than or equal to", num)
Sieve0fEratosthenes(num)

a  = 30000
for num in range(1,a+1):
    c=0
    rev=0
    temp = num
    for i in range(1,temp+1):
        if temp % i == 0:
            c += 1
    if c == 2:
        while temp > 0:
            rev = rev*10+(temp%10)
            temp //= 10
        if rev == num:
            print(num)