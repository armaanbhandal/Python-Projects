# Lab 10 - Armaan Bhandal

correct_answers = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D']

input_file = "student_solution.txt"
output_file = "test_result.txt"

try:
    with open(input_file, 'r') as file:
        student_answers = [line.strip() for line in file.readlines()]

    if len(student_answers) != 10:
        raise ValueError("The student_solution.txt file must contain exactly 10 answers.")

    correct_count = 0
    incorrect_count = 0
    correct_questions = []
    incorrect_questions = []

    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            correct_count += 1
            correct_questions.append(i + 1)
        else:
            incorrect_count += 1
            incorrect_questions.append(i + 1)

    passed = correct_count >= 7

    with open(output_file, 'w') as file:
        if passed:
            file.write("Congratulations!! You passed the exam\n")
        else:
            file.write("Sorry, you did not pass the exam\n")
        file.write(f"You answered {correct_count} questions correctly and {incorrect_count} questions incorrectly\n")
        file.write("The numbers of the questions you answered correctly are: " + " ".join(map(str, correct_questions)) + "\n")
        file.write("The numbers of the questions you answered incorrectly are: " + " ".join(map(str, incorrect_questions)) + "\n")

    print("Results successfully written to", output_file)

except FileNotFoundError:
    print(f"Error: The file {input_file} was not found. Make sure the file exists.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
