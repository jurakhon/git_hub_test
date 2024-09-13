# Task1:
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def greeting(self):
#         return f"Hello, my name is {self.name}"
#
# person1 = Person(input())
# print(person1.greeting())
#
#
# Task2:
# class Rectangle:
#     def __init__(self, a:int, b:int):
#         self.a=a
#         self.b=b
#
#     def area(self):
#         print(self.a*self.b)
#
# res=Rectangle(int(input()), int(input()))
#
# res.area()
#
#
# Task3:
# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius=radius
#
#     def show(self):
#         return f"{self.pi * self.radius**2}"
#
# obj1=Circle(4)
# print(obj1.show())
#
#
# Task4:
# class Cars:
#     total_cars = 0
#
#     def __init__(self):
#         Cars.total_cars += 1
#
#     @classmethod
#     def total_car_count(cls):
#         return cls.total_cars
#
# car1 = Cars()
# car2 = Cars()
# car3 = Cars()
#
# print(f"Total cars count: {Cars.total_car_count()}")