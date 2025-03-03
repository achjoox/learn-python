print("Welcome, Can you sign your age?")

age = int(input("Your age: "))

if age < 18:
    print("You are children")
elif age == 18:
    print("You are teenager")
else:
    print("You are adult")