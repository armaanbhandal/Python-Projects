# Assignment 08 Q02 - Armaan Bhandal

rooms = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755'}
instructors = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich'}
times = {'CS101': '8:00AM', 'CS102': '9:00AM', 'CS103': '10:00AM'}
course = input("Enter a course number: ")
if course in rooms:
    print(f"Room: {rooms[course]}, Instructor: {instructors[course]}, Time: {times[course]}")
else:
    print("Invalid course number.")
