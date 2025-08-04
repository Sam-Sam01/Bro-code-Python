# Validate user input exercise
# 1. username is no more than 12 characters
# 2. usernamee must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Username is longer than 12 characters")
elif username.find(" ") != -1:
    print("Username cannot have spaces.")
elif not username.isalpha():
    print("Username cannot contain numbers.")
else:
    print("Welcome ", username)