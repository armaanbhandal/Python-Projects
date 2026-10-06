# Assignment 07 Q07 - Armaan Bhandal

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def main():
    user_string = input("Enter a string: ")
    num_vowels = count_vowels(user_string)
    num_consonants = count_consonants(user_string)
    print(f"The string you entered includes {num_vowels} vowels and {num_consonants} consonants.")

if __name__ == "__main__":
    main()
