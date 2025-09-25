num1 = 57
num2 = 36

print("num1 & num2 =", num1 & num2)

print("\nnum1 | num2 =", num1 | num2)

print("\n~num1 =", ~num1)

print("\nnum1 ^ num2 =", num1 ^ num2)

num1 = 10
num2 = 4

print("\nnum1 >> =", num1 >> 1)

print("\nnum2 << =", num2 << 1)

num1 = 85
num2 = 62

print("\nnum1 << 1 =", num1 << 1)

print("\nnum2 >> 1 =", num2 >> 1)


def isEvenOdd(n):
    if (n ^ 1 == n + 1):
        return True
    else:
        return False
    
number = int(input("Enter your number:"))

if isEvenOdd(number):
    print(number, "is Even")
else:
    print(number, "is Odd")

def numberOfSetBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count
number = int(input("Enter your number:"))
print("Total bits : ", numberOfSetBits(number))