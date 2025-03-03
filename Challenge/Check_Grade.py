print("Hello! Wanna check your grade? (yes/no) ")

text = input("")

if text == "yes":
    grade = int(input("Input your grade here: "))
else:
    exit()

if grade >= 90 == 100:
    print("A")
elif grade >= 80 <= 89:
    print("B")
elif grade >= 70 <= 79:
    print("C")
elif grade >= 60 <= 69:
    print("D")
else:
    print("E")

exit()