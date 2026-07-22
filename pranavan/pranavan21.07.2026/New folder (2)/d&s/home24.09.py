def powerof4(number):

    count = 0

    if number > 0 and (number & (number - 1)) == 0:

        while (number > 1):

            number >>=1
            count += 1

        if (count % 2 == 0):
            return True
        else:
            return False

number = int(input("Enter your number: "))
if (powerof4(number)):
    print(number, "Yes, the number is a power of 8")
else:
    print(number, "No, the number is not a power of 8")