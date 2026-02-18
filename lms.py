# Mini Learning Management System (LMS) in Python
# Based on the project report for a console-based application using OOP

class Course:
    def __init__(self, title, lessons):
        self.title = title
        self.lessons = lessons
        self.enrolled_students = []

class Student:
    def __init__(self, name):
        self.name = name
        self.completed_lessons = {}  # key: course.title, value: number of completed lessons

def add_course(courses):
    title = input("Enter Course Title: ")
    lessons = int(input("Enter Number of lessons: "))
    new_course = Course(title, lessons)
    courses.append(new_course)
    print(f"Course '{title}' added with {lessons} lessons.")

def add_student(students):
    name = input("Enter Student name: ")
    new_student = Student(name)
    students.append(new_student)
    print(f"Student '{name}' added.")

def enroll_student(courses, students):
    student_name = input("Enter Student name: ")
    course_title = input("Enter Course title: ")
    student = next((s for s in students if s.name.lower() == student_name.lower()), None)
    course = next((c for c in courses if c.title.lower() == course_title.lower()), None)
    if student and course:
        if student not in course.enrolled_students:
            course.enrolled_students.append(student)
            print(f"Student {student.name} enrolled in {course.title}.")
        else:
            print(f"Student {student.name} is already enrolled in {course.title}.")
    else:
        print("Invalid student name or course title.")

def complete_lesson(courses, students):
    student_name = input("Enter Student name: ")
    course_title = input("Enter Course title: ")
    lesson_number = int(input("Enter number of lessons completed: "))
    student = next((s for s in students if s.name.lower() == student_name.lower()), None)
    course = next((c for c in courses if c.title.lower() == course_title.lower()), None)
    if student and course:
        student.completed_lessons[course.title] = lesson_number
        print(f"{student.name} has completed {lesson_number} lessons in {course.title}.")
    else:
        print("Invalid student name or course title.")

def course_progress(courses, students):
    student_name = input("Enter Student name: ")
    course_title = input("Enter Course title: ")
    student = next((s for s in students if s.name.lower() == student_name.lower()), None)
    course = next((c for c in courses if c.title.lower() == course_title.lower()), None)
    if student and course:
        comp = student.completed_lessons.get(course.title, 0)
        total = course.lessons
        percentage = int((comp / total) * 100) if total > 0 else 0
        print(f"Progress: {student.name} has completed {comp}/{total} lessons in {course.title} ({percentage}%).")
    else:
        print("Invalid student name or course title.")

def list_courses(courses):
    if not courses:
        print("No courses available.")
    else:
        print("Available Courses:")
        for course in courses:
            print(f"- Title: {course.title}, Lessons: {course.lessons}, Enrolled Students: {len(course.enrolled_students)}")

def list_students(students):
    if not students:
        print("No students registered.")
    else:
        print("Registered Students:")
        for student in students:
            print(f"- Name: {student.name}")

def main():
    courses = []
    students = []
    while True:
        print("\nMini Learning Management System")
        print("1. Add Course")
        print("2. Add Student")
        print("3. Enroll Student in Course")
        print("4. Record Completed Lessons")
        print("5. View Course Progress")
        print("6. List All Courses")
        print("7. List All Students")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_course(courses)
        elif choice == '2':
            add_student(students)
        elif choice == '3':
            enroll_student(courses, students)
        elif choice == '4':
            complete_lesson(courses, students)
        elif choice == '5':
            course_progress(courses, students)
        elif choice == '6':
            list_courses(courses)
        elif choice == '7':
            list_students(students)
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()