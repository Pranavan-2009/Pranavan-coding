# def intro(name):
#     print("Hello,Good moring ! I am",name)
# user_name = input("Enter your name")
# intro(user_name)



# def recur_factorial(n):
#    if n == 1:
#        return n 
#    else:
#     return n*recur_factorial(n-1)
# num = int(input("Enter a number"))


def recur_factorial(n):
   if n == 1:
       return n 
   else:
    return n*recur_factorial(n-1)
num = int(input("Enter a number"))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num ==0:
   print("The factorial of 0 is 1")
else:
   print("The factorial",num,"is",recur_factorial(num))

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

num1 = int(input("Enter Number "))
num2 = int(input("Enter Number "))

print("Sum :", add(num1, num2))
print("Difference :", subtract(num1, num2))
print("Product :", multiply(num1, num2))
print("Quotient :",divide(num1, num2))
