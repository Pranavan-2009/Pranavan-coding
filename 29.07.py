name = input("Enter your name:")
marks = int(input("Enter your marks:"))

if marks > 60:
    print("Pass")
else:
    print("Fail")


num =int(input("enter a number:"))

if num%2==0:
    print ("It is an even number")
else:
    print ("It is an odd number")

n =int(input("enter a number:"))
u =int(input("enter a number:"))
m =int(input("enter a number:"))

if n<u<m:
    print("bigest number is ",m)
elif n>u>m:
    print("bigest number is ",n)
elif n<u>m:
    print("bigest number is ",u)

balence = 100000
amount=int(input("how mach amount want to widrow:"))

if amount<balence:
    print("Widrowed")
else:
    print("low balence")

age=int(input("Enter your age:"))

if age > 18:
    print("You can vote!")
else:
    print("You can't vote!")