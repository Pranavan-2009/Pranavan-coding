from math import sqrt

def is_prime(number):
    if number > 1:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return not True
        return True
    else:
        return not True

print("Two digit prime numbers are:")
for num in range(10, 100):
    if is_prime(num):
        print(num, end=" ")
