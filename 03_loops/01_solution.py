arr = [int(x) for x in input("Enter space-separated integers: ").split()]
print("The array (list) is:", arr)

count = 0

for num in arr:
  if num > 0:
    count += 1

print("Number of positive integers in the array is:", count)