print("chai aur python")

def chai(n):
  print(n)

chai("hello chai")

name = "Chai from hello_chai"
name2 = "Chai from hello_chai"
print(name is name2)  # True, both refer to the same string object

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False, different list objects

name = (1,2,3,4,5)
name2 = (1,2,3,4,5)
print(name is name2)  # True, both refer to the same tuple object