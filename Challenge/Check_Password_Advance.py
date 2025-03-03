attempts = 3

while attempts > 0:
    print("Enter your username: ")

    username = input()

    print("Enter your password: ")

    password = input()

    if username == "admin" and password == "admin123":
        print("Hello admin! you have a full access")
        break
    elif username == "user" and password == "user123":
        print("Hello user! you have a limited access")
        break
    else:
        attempts -= 1
        print("Wrong username or password, remain {attempts} left")
    
    if attempts == 0:
        print("Too many attempts. Access denided")
exit()