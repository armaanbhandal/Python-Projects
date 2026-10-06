# Assignment 07 Q01 - Armaan Bhandal


def main():
    filename = input("Enter a filename: ")
    try:
        with open(filename, 'r') as file:
            scores = list(map(int, file.read().split()))
        print(scores)
        print(f"There are {len(scores)} scores")
        print(f"The total is {sum(scores)}")
        print(f"The average is {sum(scores) / len(scores):.2f}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()


