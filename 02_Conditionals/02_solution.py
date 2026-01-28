age = 26
day = "wednesday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    price /= 2
    
print(f"The ticket price is: ${price}")