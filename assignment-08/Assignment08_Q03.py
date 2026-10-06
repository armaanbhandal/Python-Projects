# Assignment 08 Q03 - Armaan Bhandal

DIGIT_TO_WORD = {str(i): word for i, word in enumerate(
    ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])}


def main():
    while True:
        number = input("Enter an integer to convert to words: ").strip()
        if number.isdigit():
            break
        print("Please enter digits only (for example 2025).")
    print(" ".join(DIGIT_TO_WORD[digit] for digit in number))


if __name__ == "__main__":
    main()
