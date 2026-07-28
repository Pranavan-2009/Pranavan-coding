name = input("Enter your name: ")
marks = float(input("Enter your marks: "))



if marks < 100:
    print("A")
elif marks < 75:
    print("B")
elif marks < 65:
    print("C")
elif marks < 50:
    print("C")
elif marks < 35:
    print("S")
elif marks < 0:
    print("Fail")





city = input("Enter your city name: ")
temp = float(input("Enter today's temperature in C: "))



if temp > 35:
    print("Warning: It is very hot today!")

if temp > 25:
    print("Great day to go outside!")
else:
    print("Grab a jacket before you go out!")

if temp > 35:
    print("weather:scorching Hot")
elif temp > 25:
    print("weather: warm and sunny")
elif temp > 15:
    print("weather:cool and breezy")

import datetime
import calendar

now =datetime.datetime.now()
print("City:",city)
print("Time now:",now)

print(calendar.calendar(now.year))