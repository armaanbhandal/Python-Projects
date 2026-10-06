# Assignment 07 Q03 - Armaan Bhandal

def main():
    with open("BoyNames.txt", "r") as boys_file, open("GirlNames.txt", "r") as girls_file:
        boys = set(boys_file.read().splitlines())
        girls = set(girls_file.read().splitlines())

    boy_name = input("Enter a boy's name, or N if you do not wish to enter a boy's name: ")
    girl_name = input("Enter a girl's name, or N if you do not wish to enter a girl's name: ")

    if boy_name != "N":
        if boy_name in boys:
            print(f"{boy_name} is one of the most popular boy's names.")
        else:
            print(f"{boy_name} is not one of the most popular boy's names.")
    else:
        print("You chose not to enter a boy's name.")

    if girl_name != "N":
        if girl_name in girls:
            print(f"{girl_name} is one of the most popular girl's names.")
        else:
            print(f"{girl_name} is not one of the most popular girl's names.")
    else:
        print("You chose not to enter a girl's name.")

if __name__ == "__main__":
    main()
