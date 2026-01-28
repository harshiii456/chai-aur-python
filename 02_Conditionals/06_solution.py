dist = int(input("Enter the distance to travel (in km): "))

if dist < 3:
  transport = "walk"
elif 3 <= dist <= 15:
  transport = "bike"
else:
  transport = "car"

print(transport)