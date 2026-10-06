# Lab 10 - Armaan Bhandal

CORRECT_ANSWERS = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D']
PASSING_SCORE = 7

INPUT_FILE = "student_solution.txt"
OUTPUT_FILE = "test_result.txt"


def main():
    try:
        with open(INPUT_FILE, 'r') as file:
            # Ignore blank lines and accept lowercase answers
            student_answers = [line.strip().upper() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {INPUT_FILE} was not found. Make sure the file exists.")
        return

    if len(student_answers) != len(CORRECT_ANSWERS):
        print(f"Error: {INPUT_FILE} must contain exactly {len(CORRECT_ANSWERS)} answers, "
              f"one per line (found {len(student_answers)}).")
        return

    correct_questions = []
    incorrect_questions = []
    for number, (given, expected) in enumerate(zip(student_answers, CORRECT_ANSWERS), start=1):
        if given == expected:
            correct_questions.append(number)
        else:
            incorrect_questions.append(number)

    passed = len(correct_questions) >= PASSING_SCORE

    with open(OUTPUT_FILE, 'w') as file:
        if passed:
            file.write("Congratulations!! You passed the exam\n")
        else:
            file.write("Sorry, you did not pass the exam\n")
        file.write(f"You answered {len(correct_questions)} questions correctly and "
                   f"{len(incorrect_questions)} questions incorrectly\n")
        file.write("The numbers of the questions you answered correctly are: "
                   + " ".join(map(str, correct_questions)) + "\n")
        file.write("The numbers of the questions you answered incorrectly are: "
                   + " ".join(map(str, incorrect_questions)) + "\n")

    print("Results successfully written to", OUTPUT_FILE)


if __name__ == "__main__":
    main()
