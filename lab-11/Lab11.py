# Lab 11 - Armaan Bhandal

def readMessages(filename):
    with open(filename, 'r') as file:
        messages = file.readlines()
    return [message.strip() for message in messages]

def encryptMessages(messages):
    encrypted_messages = []
    for message in messages:
        encrypted_message = ''
        for char in message:
            if char.isalpha():
                shift = 3
                if char.islower():
                    encrypted_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                elif char.isupper():
                    encrypted_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_message += char
        encrypted_messages.append(encrypted_message)

    with open('encrypted_messages.txt', 'w') as file:
        for encrypted_message in encrypted_messages:
            file.write(encrypted_message + '\n')

def decryptMessages(filename):
    with open(filename, 'r') as file:
        encrypted_messages = file.readlines()

    decrypted_messages = []
    for message in encrypted_messages:
        decrypted_message = ''
        for char in message.strip():
            if char.isalpha():
                shift = 3
                if char.islower():
                    decrypted_message += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                elif char.isupper():
                    decrypted_message += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_message += char
        decrypted_messages.append(decrypted_message)

    print("Decrypted messages:")
    for message in decrypted_messages:
        print(message)

def main():
    input_filename = input("Enter the input filename containing the original messages: ").strip()
    try:
        messages = readMessages(input_filename)
    except FileNotFoundError:
        print(f"File not found: {input_filename}")
        return
    encryptMessages(messages)
    decryptMessages('encrypted_messages.txt')

if __name__ == '__main__':
    main()
