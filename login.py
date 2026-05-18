
original_username = input("Create username: ")
original_password = input("Create password: ")

print("\n--- Login ---")

for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == original_username and password == original_password:
        print("Login Successful")
        break
    else:
        print("Wrong Username or Password")

else:
    print("Too many attempts. Access Denied")

