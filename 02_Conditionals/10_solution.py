animal = input("Enter an animal: ")
age = int(input("Enter the age of the animal: "))

if animal.lower() == "dog":
    if age < 2:
        print("give puppy food")
    else:
        print("give adult dog food")
elif animal.lower() == "cat":
    if age < 5:
        print("give kitten food")
    else:
        print("give adult cat food")
        