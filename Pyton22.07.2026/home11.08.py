num = int(input("Enter a number: "))

if num >= 0:
    num_str = str(num)
    order = len(num_str)
    
    total = 0
    for i in range(0, order):
        digit = int(num_str[i])
        total = total + (digit ** order)
        
    if total == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")



