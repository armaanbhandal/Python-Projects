# Assignment 08 Q07 - Armaan Bhandal

CODES = {'A': ')', 'a': '0', 'B': '(', 'b': '9', 'C': '*', 'c': '8',
         'D': '&', 'd': '7', 'E': '^', 'e': '6', 'F': '%', 'f': '5',
         'G': '$', 'g': '4', 'H': '#', 'h': '3', 'I': '@', 'i': '2',
         'J': '!', 'j': '1', 'K': 'Z', 'k': 'z', 'L': 'Y', 'l': 'y',
         'M': 'X', 'm': 'x', 'N': 'W', 'n': 'w', 'O': 'V', 'o': 'v',
         'P': 'U', 'p': 'u', 'Q': 'T', 'q': 't', 'R': 'S', 'r': 's',
         'S': 'R', 's': 'r', 'T': 'Q', 't': 'q', 'U': 'P', 'u': 'p',
         'V': 'O', 'v': 'o', 'W': 'N', 'w': 'n', 'X': 'M', 'x': 'm',
         'Y': 'L', 'y': 'l', 'Z': 'K', 'z': 'k'}


def main():
    input_file = input("Enter the input file: ").strip()
    output_file = input("Enter the output file: ").strip()

    try:
        with open(input_file, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return

    encrypted = ''.join(CODES.get(char, char) for char in text)
    with open(output_file, 'w') as file:
        file.write(encrypted)
    print(f"Encrypted text saved to {output_file}.")


if __name__ == "__main__":
    main()
