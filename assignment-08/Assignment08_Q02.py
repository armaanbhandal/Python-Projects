# Assignment 08 Q02 - Armaan Bhandal

ROOMS = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755'}
INSTRUCTORS = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich'}
TIMES = {'CS101': '8:00AM', 'CS102': '9:00AM', 'CS103': '10:00AM'}


def main():
    course = input("Enter a course number: ").strip().upper()
    if course in ROOMS:
        print(f"Room: {ROOMS[course]}, Instructor: {INSTRUCTORS[course]}, Time: {TIMES[course]}")
    else:
        print(f"Invalid course number. Valid courses: {', '.join(ROOMS)}")


if __name__ == "__main__":
    main()
