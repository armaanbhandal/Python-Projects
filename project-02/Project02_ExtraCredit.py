# Project 02 ExtraCredit - Armaan Bhandal

def load_data(file_name):
    data = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, email = line.strip().split(':')
                data[name] = email
    except (FileNotFoundError, ValueError):
        pass 
    return data

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        for name, email in data.items():
            file.write(f"{name}:{email}\n")

def display_menu():
    print("\nMenu")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")

def look_up(data):
    name = input("Enter a name: ")
    if name in data:
        print(f"Name: {name}, Email: {data[name]}")
    else:
        print("The specified name was not found.")

def add_entry(data):
    name = input("Enter name: ")
    if name in data:
        print("That name already exists.")
    else:
        email = input("Enter email address: ")
        data[name] = email
        print("Name and address have been added.")

def change_email(data):
    name = input("Enter name: ")
    if name in data:
        email = input("Enter the new email address: ")
        data[name] = email
        print("Information updated.")
    else:
        print("The specified name was not found.")

def delete_entry(data):
    name = input("Enter name: ")
    if name in data:
        del data[name]
        print("Information deleted.")
    else:
        print("The specified name was not found.")

def main():
    file_name = "contacts.txt"
    data = load_data(file_name)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            look_up(data)
        elif choice == "2":
            add_entry(data)
        elif choice == "3":
            change_email(data)
        elif choice == "4":
            delete_entry(data)
        elif choice == "5":
            save_data(file_name, data)
            print("Information saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
