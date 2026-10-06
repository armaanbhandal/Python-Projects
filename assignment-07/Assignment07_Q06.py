# Assignment 07 Q06 - Armaan Bhandal

import random
import string

MAX_LENGTH = 10000

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def main():
    while True:
        try:
            length = int(input("Enter length of a string: "))
            if not 0 <= length <= MAX_LENGTH:
                raise ValueError
            break
        except ValueError:
            print(f"Please enter a whole number from 0 to {MAX_LENGTH}.")
    print(f"The random string is: {random_string(length)}")

if __name__ == "__main__":
    main()
