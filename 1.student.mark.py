class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = Student(id, name, dob)
        self.students.append(student)

    def add_course(self):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(id, name)
        self.courses.append(course)

    def add_mark(self):
        course_id = input("Enter course ID: ")
        for student in self.students:
            if student.id == input("Enter student ID: "):
                mark = int(input("Enter student mark: "))
                student.add_mark(course_id, mark)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"{course.id}: {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"{student.id}: {student.name}")

    def show_student_marks(self):
        course_id = input("Enter course ID: ")
        print(f"Marks for course {course_id}:")
        for student in self.students:
            if course_id in student.marks:
                print(f"{student.name}: {student.marks[course_id]}")

manager = StudentMarkManagement()

num_students = int(input("Enter number of students: "))
for i in range(num_students):
    manager.add_student()

num_courses = int(input("Enter number of courses: "))
for i in range(num_courses):
    manager.add_course()

while True:
    print("Select an option:")
    print("1. Add mark")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a course")
    print("5. Quit")
    choice = int(input())
    if choice == 1:
        manager.add_mark()
    elif choice == 2:
        manager.list_courses()
    elif choice == 3:
        manager.list_students()
    elif choice == 4:
        manager.show_student_marks()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
