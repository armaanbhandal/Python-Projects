# Assignment 07 Q05 - Armaan Bhandal

def main():
    filename = input("Enter a filename: ")
    string_to_remove = input("Enter a string to be removed: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        updated_content = content.replace(string_to_remove, '')

        with open(filename, 'w') as file:
            file.write(updated_content)

        print("String removed successfully.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
