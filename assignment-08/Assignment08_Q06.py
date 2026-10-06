# Assignment 08 Q06 - Armaan Bhandal

import string
filename = input("Enter the file name: ")
with open(filename, 'r') as file:
    text = file.read().lower()
counts = {char: text.count(char) for char in string.ascii_lowercase}
print("LETTER\tCOUNT")
for char, count in sorted(counts.items()):
    print(f"{char}\t{count}")
