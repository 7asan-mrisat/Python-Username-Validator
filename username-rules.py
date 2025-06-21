while True:  # This creates an infinite loop
    username = input("Enter Your Username : ")
# user's username cant be les sthan 8 characters so
    if len(username) < 8: 
        print("Username should be at least 8 characters long ❌")
    # user's username cannot contain spaces so
    elif ' ' in username:
        print("Username should not contain spaces ❌")
    elif not username.isalpha():
        print("Username should only contain alphabetical characters 🔠")
    else : 
        print (f"{username} is a valid username ✔")
        break
