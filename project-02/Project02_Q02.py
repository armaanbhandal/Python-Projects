# Project 02 Q02 - Armaan Bhandal

import string

def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))

def read_file(file_name):
    words = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                for word in line.split():
                    words.append(remove_punctuation(word.lower()))
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return words

def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        for line in data:
            file.write(line + '\n')

def unique_words(words):
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return result

def union_words(words1, words2):
    result = []
    for word in words1:
        if word not in result:
            result.append(word)
    for word in words2:
        if word not in result:
            result.append(word)
    return result

def common_words(words1, words2):
    result = []
    for word in words1:
        if word in words2 and word not in result:
            result.append(word)
    return result

def difference_words(words1, words2):
    result = []
    for word in words1:
        if word not in words2 and word not in result:
            result.append(word)
    return result

def word_count(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def format_frequency_table(word_counts):
    table = []
    for word, count in sorted(word_counts.items()):
        table.append(f"{word}: {count}")
    return table

def main():
    file1 = input("Enter the name of the first input file: ")
    file2 = input("Enter the name of the second input file: ")

    words1 = read_file(file1)
    words2 = read_file(file2)

    unique_words_file1 = unique_words(words1)
    unique_words_file2 = unique_words(words2)
    union = union_words(words1, words2)
    common = common_words(words1, words2)
    diff_file1 = difference_words(words1, words2)
    diff_file2 = difference_words(words2, words1)
    exclusive = difference_words(union, common)
    frequency1 = word_count(words1)
    frequency2 = word_count(words2)

    output = [
        "Unique words in the first file:",
        *unique_words_file1,
        "",
        "Unique words in the second file:",
        *unique_words_file2,
        "",
        "Words in both files (union):",
        *union,
        "",
        "Common words in both files:",
        *common,
        "",
        "Words in the first file but not in the second:",
        *diff_file1,
        "",
        "Words in the second file but not in the first:",
        *diff_file2,
        "",
        "Words in either file but not both (exclusive):",
        *exclusive,
        "",
        "Frequency table for the first file:",
        *format_frequency_table(frequency1),
        "",
        "Frequency table for the second file:",
        *format_frequency_table(frequency2),
    ]

    write_to_file("fileAnalysis.txt", output)
    print("Data saved in fileAnalysis.txt")

if __name__ == "__main__":
    main()
