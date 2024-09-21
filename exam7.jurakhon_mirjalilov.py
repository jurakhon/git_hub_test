# question1:
# oop - object oriented programming mano dorad. encapsulation, abstraction, inheritance,
#
# question2:
# getter va setter baroi encapsulyatsiya istifoda burda meshavad. baroi private variable dostup kushodoan istifoda mebarem.
# yane mo metonem if condition kati dostup tiyem yoki @property kati elegantniy dostup metiyem.
#
#
# question3:
# @classmethod
#
# question4:
# constructor in classro mesozad bo __new__ va initsiaylizatsiya mekunad bo __init__
# destructor boshad __del__ in objectro az pamyat udalit mekunad.
#
# question5:
# global ba hama vidimost dorad. agar yak element global boshad digar method yo funksiyaho dida metonad vay elementro .
# local variable hamu variable meboshad ki dar daruni hamu funksiya meboshad ba xud local meboshad. yani baroi xudash  bay local
# meboshad. nonlocal dar funkiyai beruna maasalan guyem a =5 boshad, funksiyai darunada  nonlocal a guyem a=5 ro dar innner istifoda burda
#     metonemm
#





# Task1:
# x = int(input())
# y = int(input())
#
# for i in range(x, y+1):
#     for j in range(1, 11):
#         print(f"{i}x{j}={i*j}")
#     print()


# Task2:
# class Circle:
#     PI = 3.1415
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return f" area = {2 * self.PI * self.radius * self.radius}"
#
#     def get_diameter(self):
#         return f"diameter = {2 * self.radius}"
#
#     def get_circumference(self):
#         return f"circumference = {2*self.PI*self.radius}"
#
#     def get_radius(self):
#         return f"radius = {self.radius}"
#
# obj1 = Circle(2)
# print(obj1.get_area())
# print(obj1.get_diameter())
# print(obj1.get_circumference())
# print(obj1.get_radius())




# Task5:
# from datetime import datetime
#
# database = []
#
#
#
# class Course:
#     def __init__(self, student_fullname, student_id, student_course_name, grades, student_attendance ):
#         self.student_fullname = student_fullname
#         self.student_id = student_id
#         self.student_course_name = student_course_name
#         self.student_grades = grades
#         self.student_attendance = student_attendance
#
#     def __str__(self):
#         return f"Fullname: {self.student_fullname} Student ID: {self.student_id}, Course: {self.student_course_name}, Grades: {self.student_grades} Attendance: {self.student_attendance}"
#
#
# class CourseManager:
#     def add_student(self):
#         new_student = Course(
#             input("Student Fullname: "),
#             input("Student ID: "),
#             input("Student Course:"),
#             input("Student Grades:"),
#             input("Student Attendance:"),
#         )
#         database.append(new_student)
#
#     def get_all_students(self):
#         for students in database:
#             print(students)
#
#     def get_student_by_id(self, id):
#         for student in database:
#             if student.student_id == id:
#                 return student
#
#     def edit_course(self, id):
#         student = self.get_student_by_id(id)
#         new_course = input("enter new course")
#         student.student_course_name = new_course
#         print(f"Course updated successfully for student {student.student_fullname}")
#
#     def edit_grades(self, id):
#         student = self.get_student_by_id(id)
#         new_grades = input(f"enter new grade for {student.student_fullname} and update grade {student.student_grades}")
#         student.student_grades = new_grades
#         print(f"Grades updated successfully for student {student.student_fullname}")
#
#     def del_student_by_id(self,id):
#         for student in database:
#             if student.student_id == id:
#                 database.remove(student)
#                 print(f"{student.student_fullname} has been removed from database")
#
#
# courseman = CourseManager()
#
# while True:
#     user_input = int(input("1. add new student info: \n"
#                            "2. print all student details: \n"
#                            "3. edit course by id \n"
#                            "4. edit grades by id \n"
#                            "5. delete student with id: \n"
#                            "6. exit: " ))
#     if user_input == 1:
#         courseman.add_student()
#
#     elif user_input == 2:
#         courseman.get_all_students()
#
#     elif user_input == 3:
#         courseman.edit_course(input("enter student id: "))
#
#     elif user_input == 4:
#         courseman.edit_grades(input("enter student id: "))
#
#     elif user_input == 5:
#         courseman.del_student_by_id(input("enter id of the student you want to delete:"))
#
#     elif user_input == 6:
#         print("Exiting program. Good bye!")
#         break


# Task6:
# from datetime import datetime
# from os import remove
# from traceback import print_tb
#
# lst = []
# database = []
# global_user = None
#
# class User:
#     def __init__(self, firstname, lastname, email, username, password):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.email = email
#         self.username = username
#         self.password = password
#
#
#     def __str__(self):
#         return f"{self.firstname} {self.lastname} {self.email} username:{self.username}"
#
#
# class UserManager:
#     def add_new_user(self):
#         new_user = User(
#             input("Enter firstname: "),
#             input("Enter lastname: "),
#             input("Enter email: "),
#             input("Enter username: "),
#             input("Enter password: ")
#         )
#         lst.append(new_user)
#
#     def login(self, username_check, password_check):
#         for user in lst:
#             if username_check == user.username and password_check == user.password:
#                 global global_user
#                 global_user = username_check
#                 return "Login successful"
#             else:
#                 return "Wrong password or username"
#
#     def logout(self):
#         return "You have been logged out. Good Bye!"
#
#     def change_password(self, new_pass):
#         self.new_pass = new_pass
#         for user in lst:
#             if user.password in lst:
#                 user.password = new_pass
#
#     def get_info(self):
#         for user in lst:
#             print(user)
#
# usermanager = UserManager()
#
#
#
# while True:
#     print(f"You are logged in as {global_user}")
#     a = input("1. Register\n"
#               "2. Login\n"
#               "3. change password\n "
#               "4. print list\n "
#               "5. Logout\n"
#               "8. Exit\n"
#               "Choose an option: ")
#     if a == "1":
#         usermanager.add_new_user()
#         print("Registration successful!")
#         for user in lst:
#             print(user)
#     elif a == "2":
#         res = usermanager.login(input("Enter username: "), input("Enter password: "))
#         print(res)
#
#     elif a == "3":
#         usermanager.change_password(input("enter new pass "))
#
#     elif a == "4":
#         usermanager.get_info()
#     elif a == "5":
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid option. Please try again.")


# Task4:
# class Calculator:
#     def __init__(self, firstnum, operator, secondnum):
#         self.firstnum = firstnum
#         self.operator = operator
#         self.secondnum = secondnum
#
#     def Sum(self):
#         return f"{self.firstnum} + {self.secondnum} = {self.firstnum+self.secondnum}"
#
#     def Subtract(self):
#         return f"{self.firstnum} - {self.secondnum} = {self.firstnum-self.secondnum}"
#
#     def Multiplication(self):
#         return f"{self.firstnum} * {self.secondnum} = {self.firstnum * self.secondnum}"
#
#     def Division(self):
#         return f"{self.firstnum} / {self.secondnum} = {self.firstnum/self.secondnum}"
#
# calc = Calculator()


# Task3:
# class Calculator:
#
#     @staticmethod
#     def factorial(n):
#         if n < 0:
#             return "Factorial is not defined for negative numbers"
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#
#     @staticmethod
#     def power(a, b):
#         result = 1
#         for i in range(b):
#             result *= a
#         return result
#
#     @staticmethod
#     def sqrt(n):
#         if n < 0:
#             return "Square root is not defined for negative numbers"
#         guess = n / 2.0
#         tolerance = 0.00001
#         while abs(guess * guess - n) > tolerance:
#             guess = (guess + n / guess) / 2.0
#         return guess


