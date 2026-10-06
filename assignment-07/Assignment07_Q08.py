# Assignment 07 Q08 - Armaan Bhandal

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not password.isalnum():
        return False
    if sum(char.isdigit() for char in password) < 2:
        return False
    return True

def main():
    password = input("Enter a string for password: ")
    if is_valid_password(password):
        print("Valid password")
    else:
        print("Invalid password")

if __name__ == "__main__":
    main()
