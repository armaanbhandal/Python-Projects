# Assignment 07 Q06 - Armaan Bhandal

import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def main():
    length = int(input("Enter length of a string: "))
    print(f"The random string is: {random_string(length)}")

if __name__ == "__main__":
    main()
