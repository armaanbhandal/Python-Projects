# Assignment 08 Q04 - Armaan Bhandal

capitals = {}
while True:
    entry = input("Enter a country and capital (Q to quit): ")
    if entry.upper() == "Q":
        break
    country, capital = map(str.strip, entry.split(","))
    capitals[country] = capital
print("COUNTRY\t\tCAPITAL")
for country, capital in sorted(capitals.items()):
    print(f"{country}\t\t{capital}")
