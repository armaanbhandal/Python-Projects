# Assignment 07 Q01 - Armaan Bhandal


def main():
    filename = input("Enter a filename: ")
    try:
        with open(filename, 'r') as file:
            scores = list(map(int, file.read().split()))
    except FileNotFoundError:
        print("File not found.")
        return
    except ValueError:
        print("The file must contain only whole-number scores separated by spaces or lines.")
        return

    if not scores:
        print("The file contains no scores.")
        return

    print(scores)
    print(f"There are {len(scores)} scores")
    print(f"The total is {sum(scores)}")
    print(f"The average is {sum(scores) / len(scores):.2f}")

if __name__ == "__main__":
    main()


