#login.py
def login(username, password):
    # Predefined credentials (for demo purpose)
    stored_username = "branch2"
    stored_password = "admin123"

    if username == stored_username and password == stored_password:
        return "Login successful"
    else:
        return "Invalid username or password"
# Test the login feature
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    result = login(user, pwd)
    print(result)


