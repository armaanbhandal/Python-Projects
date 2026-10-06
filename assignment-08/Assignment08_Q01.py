# Assignment 08 Q01 - Armaan Bhandal

data = {'a': 15, 'c': 35, 'b': 10}
print("Keys:", data.keys())
print("Values:", data.values())
print("Key-Value pairs:")
for key, value in data.items():
    print(f"{key}\t{value}")
print("Sorted by keys:")
for key in sorted(data.keys()):
    print(f"{key}\t{data[key]}")
print("Sorted by values:")
for key in sorted(data, key=data.get):
    print(f"{key}\t{data[key]}")
