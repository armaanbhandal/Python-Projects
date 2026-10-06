# Assignment 08 Q04 - Armaan Bhandal


def main():
    capitals = {}
    while True:
        entry = input("Enter a country and capital (Q to quit): ").strip()
        if entry.upper() == "Q":
            break
        parts = [part.strip() for part in entry.split(",")]
        if len(parts) != 2 or not all(parts):
            print("Please enter them as: Country, Capital")
            continue
        country, capital = parts
        capitals[country] = capital

    if not capitals:
        print("No countries entered.")
        return

    print("COUNTRY\t\tCAPITAL")
    for country, capital in sorted(capitals.items()):
        print(f"{country}\t\t{capital}")


if __name__ == "__main__":
    main()
