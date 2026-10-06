# Assignment 08 Q06 - Armaan Bhandal

import string


def main():
    filename = input("Enter the file name: ").strip()
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    counts = {char: text.count(char) for char in string.ascii_lowercase}

    print("LETTER\tCOUNT")
    for char, count in sorted(counts.items()):
        print(f"{char}\t{count}")


if __name__ == "__main__":
    main()
