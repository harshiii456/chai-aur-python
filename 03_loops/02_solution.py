num = int(input("Enter a positive integer: "))

sum = 0

for i in range(1, num + 1):
    if (i % 2 == 0):
        sum = sum + i

print("The sum of even numbers from 1 to", num, "is:", sum)