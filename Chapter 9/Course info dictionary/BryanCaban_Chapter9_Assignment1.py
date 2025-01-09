# Course Dictionary Program
# Program that lets a user enter a course code and then prints the course name, descirption, course_info.instructor, and number of students, ect.

# Dictionary containing course numbers and room numbers
room_numbers = {
    "CS101": 3004,
    "CS102": 4501,
    "CS103": 6755,
    "NT110": 1244,
    "CM241": 1411
}

# Dictionary containing course numbers and instructor names
instructors = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

# Dictionary containing course numbers and meeting times
meeting_times = {
    "CS101": "8:00 a.m.",
    "CS102": "9:00 a.m.",
    "CS103": "10:00 a.m.",
    "NT110": "11:00 a.m.",
    "CM241": "1:00 p.m."
}

# Def that asks if the user wants to run the code
def runcode():
    runcode = str(input('\nDo you want to run this code?(Yes/No): '))
    return runcode

# Def that checks for the course code and what the room is for that course
def get_course_info(course_number):
    # Check if the course number exists in the dictionaries
    if course_number in room_numbers and course_number in instructors and course_number in meeting_times:
        # Display course information
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room_numbers[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting Time: {meeting_times[course_number]}")
    else:
        print("Course not found.")

# Def uses the value to return the course info to the user
def main():
    print('Welcome to the Course Dictionary Program!')
    print('This program will let you look up information about a course.')
    print('Enter the course code for the course you want to look up.')
    
    course_number = input("Enter the course number (e.g., CS101): ").strip().upper()
    get_course_info(course_number)

# Code that runs when the user wants to run the code
while runcode().casefold() == 'yes':
    main()

# If the user does not want to run the code this will happen.
else:
    print('Code did not run. Thank You.')

# Program started on Oct 22, 2024 by Bryan Caban