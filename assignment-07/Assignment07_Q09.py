# Assignment 07 Q09 - Armaan Bhandal

def is_anagram(s1, s2):
    count1 = {}
    count2 = {}

    for char in s1:
        if char.isalpha():
            count1[char.lower()] = count1.get(char.lower(), 0) + 1

    for char in s2:
        if char.isalpha():
            count2[char.lower()] = count2.get(char.lower(), 0) + 1

    return count1 == count2

def main():
    word1 = input("Enter the first string: ")
    word2 = input("Enter the second string: ")

    if is_anagram(word1, word2):
        print(f"{word1} and {word2} are anagram.")
    else:
        print(f"{word1} and {word2} are not anagram.")

if __name__ == "__main__":
    main()
