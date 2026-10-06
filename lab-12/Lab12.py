# Lab 12 - Armaan Bhandal

def relatives(people, family_name):
    return [first_name for first_name, last_name in people.items() if last_name == family_name]

def main():
    print("Enter 6 names (First and Last):")
    people = {}
    for i in range(6):
        while True:
            parts = input(f"Name {i + 1}: ").split()
            if len(parts) == 2:
                break
            print("Please enter exactly a first and last name, like: Jane Smith")
        first_name, last_name = parts
        people[first_name] = last_name

    family_name = input("\nEnter family name: ").strip()

    print("\nFirst Name     Last NAME")
    print("------------------------")
    for first_name, last_name in people.items():
        print(f"{first_name:<15}{last_name:<15}")

    matching_names = relatives(people, family_name)

    if matching_names:
        print(f"\nPersons with the same last name, {family_name}:")
        for name in matching_names:
            print(name)
    else:
        print(f"\nNo persons with the same last name.")

if __name__ == "__main__":
    main()
