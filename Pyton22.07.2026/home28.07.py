passenger_name = "Raj"
price = 45.00
quantity = 2
is_available = True

print("Passenger:", passenger_name)
print("Price: $", price)
print("Tickets Booked:", quantity)
print("Available?", is_available)

print(type(passenger_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 5.00)
print("Double tickets:", quantity * 2)

print("Is price under $50?", price < 50)
print("More than 5 tickets?", quantity > 5)
print("Is price exactly $45.00?", price == 45.00)

counter_name = "Express" + "" + "Bus"
print("Counter name:", counter_name)
print("Letters in passenger name:", len(passenger_name))
print("First letter:", passenger_name[0])

price_a = 45.00
price_b = 90.00
print("Before:", price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After:", price_a, "and", price_b)