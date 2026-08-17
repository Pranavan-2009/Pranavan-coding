num = int(input("Enter the number of terms: "))

if num > 0:
    first = 0
    second = 1
    
    print("Fibonacci series:")
    for i in range(0, num):
        print(first)
        next_num = first + second
        first = second
        second = next_num
else:
    print("Please enter a positive number.")