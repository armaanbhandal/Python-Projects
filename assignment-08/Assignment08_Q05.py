# Assignment 08 Q05 - Armaan Bhandal


def main():
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()

    first_letters = set(first_name)
    last_letters = set(last_name)

    print("Intersection:", sorted(first_letters & last_letters))
    print("Union:", sorted(first_letters | last_letters))
    print("Symmetric Difference:", sorted(first_letters ^ last_letters))


if __name__ == "__main__":
    main()
