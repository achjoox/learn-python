print("Enter your username: ")

username = input(str(""))

print("Enter your password: ")

password = input("")

if username == "admin" and password == "admin123":
    print("Welcome admin! You have full access")
elif username == "user" and password == "user123":
    print("Welcome user! You have limited access")
elif username != "user" and username != "admin":
    print("Wrong user")
elif password != "admin123" and password != "user123":
    print("Wrong Password")
exit()