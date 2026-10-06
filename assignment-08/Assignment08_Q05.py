# Assignment 08 Q05 - Armaan Bhandal

first_name = input("Enter first name: ").lower()
last_name = input("Enter last name: ").lower()
print("Intersection:", set(first_name) & set(last_name))
print("Union:", set(first_name) | set(last_name))
print("Symmetric Difference:", set(first_name) ^ set(last_name))
