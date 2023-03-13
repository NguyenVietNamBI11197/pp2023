class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob
        self._marks = {}

    def add_mark(self, course_id, mark):
        self._marks[course_id] = mark

    def get_marks(self):
        return self._marks

    def __str__(self):
        return f"{self._id}: {self._name}"

class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def __str__(self):
        return f"{self._id}: {self._name}"

class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []

    def add_student(self):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = Student(id, name, dob)
        self._students.append(student)

    def add_course(self):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(id, name)
        self._courses.append(course)

    def add_mark(self):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID: ")
        for student in self._students:
            if student._id == student_id:
                mark = int(input("Enter student mark: "))
                student.add_mark(course_id, mark)

    def list_courses(self):
        print("Courses:")
        for course in self._courses:
            print(course)

    def list_students(self):
        print("Students:")
        for student in self._students:
            print(student)

    def show_student_marks(self):
        course_id = input("Enter course ID: ")
        print(f"Marks for course {course_id}:")
        for student in self._students:
            if course_id in student.get_marks():
                print(f"{student}: {student.get_marks()[course_id]}")

    def input(self):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            self.add_student()

        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            self.add_course()

    def list(self):
        while True:
            print("Select an option:")
            print("1. List courses")
            print("2. List students")
            print("3. Show student marks for a course")
            print("4. Quit")
            choice = int(input())
            if choice == 1:
                self.list_courses()
            elif choice == 2:
                self.list_students()
            elif choice == 3:
                self.show_student_marks()
            elif choice == 4:
                break
            else:
                print("Invalid choice")

    def run(self):
        self.input()
        self.list()

manager = StudentMarkManagement()
manager.run()
