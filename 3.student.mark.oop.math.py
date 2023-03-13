import math
import curses
import numpy as np


class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob
        self._marks = {}

    def add_mark(self, course_id, mark):
        self._marks[course_id] = math.floor(mark*10)/10  # round down to 1 decimal place

    def get_marks(self):
        return self._marks

    def __str__(self):
        return f"{self._id}: {self._name}"


class Course:
    def __init__(self, id, name, credits):
        self._id = id
        self._name = name
        self._credits = credits

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
        credits = int(input("Enter course credits: "))
        course = Course(id, name, credits)
        self._courses.append(course)

    def add_mark(self):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID: ")
        for student in self._students:
            if student._id == student_id:
                mark = float(input("Enter student mark: "))
                student.add_mark(course_id, mark)

    def calculate_gpa(self, student):
        total_credits = 0
        weighted_sum = 0
        for course in self._courses:
            if course._id in student.get_marks():
                credits = course._credits
                mark = student.get_marks()[course._id]
                total_credits += credits
                weighted_sum += credits * mark
        if total_credits == 0:
            return 0
        else:
            return weighted_sum / total_credits

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

    def sort_students_by_gpa(self):
        self._students.sort(key=lambda student: self.calculate_gpa(student), reverse=True)

    def display_students_by_gpa(self, screen):
        screen.clear()
        screen.addstr(0, 0, "Students sorted by GPA (descending):")
        for i, student in enumerate(self._students):
            gpa = self.calculate_gpa(student)
            screen.addstr(i+1, 0, f"{student}: {gpa:.2f}")
        screen.refresh()

    def input(self):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            self.add_student()

        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            self.add_student()