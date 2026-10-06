# Assignment 08 Q03 - Armaan Bhandal

digit_to_word = {str(i): word for i, word in enumerate(
    ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])}
number = input("Enter an integer to convert to words: ")
print(" ".join(digit_to_word[digit] for digit in number))
