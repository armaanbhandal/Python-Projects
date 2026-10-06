# Assignment 07 Q10 - Armaan Bhandal

def scramble2_encrypt(text):
    return text[1::2] + text[0::2]

def scramble2_decrypt(text):
    half = len(text) // 2
    odds = text[:half]   # characters that were at odd positions
    evens = text[half:]  # characters that were at even positions
    result = ''.join(e + o for e, o in zip(evens, odds))
    if len(evens) > len(odds):
        result += evens[-1]
    return result

def process_file(input_file, output_file, mode):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

        if mode == 'E':
            encrypted = scramble2_encrypt(content)
            with open(output_file, 'w') as outfile:
                outfile.write(encrypted)
        elif mode == 'D':
            decrypted = scramble2_decrypt(content)
            with open(output_file, 'w') as outfile:
                outfile.write(decrypted)

        print("Done")
    except FileNotFoundError:
        print("File not found.")

def main():
    input_file = input("Enter a source filename: ")
    output_file = input("Enter a target filename: ")
    mode = input("Enter E to encrypt or D to decrypt the input file: ").upper()

    if mode in ('E', 'D'):
        process_file(input_file, output_file, mode)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
