
# Task1:
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary
#
#     def show(self):
#             return  f"{self.name} {self._salary}"
#
#
# myobj=Employee("Muhammad",10000 )
#
#
# print(myobj.name) # print mekunad baroi on ki public meboshad
# print(myobj._salary) # print mekunad baroi on ki protected meboshad. dar python nishon medihad lekin tavsiya doda nameshavad.


# Task2:
# class BankAccount:
#     def __init__(self, balance, pin):
#         self._balance = balance
#         self.__pin = pin
#
#     def show(self):
#             return  f"{self._balance} {self.__pin}"
#
#
# myobj=BankAccount(10000,12345 )
#
# #print(myobj.show())
# print(myobj._balance) # nishon medihad baroi on ki protected. lekin tavsiya doda nameshavad dar pep8.
# print(myobj.__pin) # nishon namedihad baroi on ki private meboshad.


# Task3:
# a)
# class BankAccount:
#     def __init__(self, balance, pin):
#         self._balance = balance
#         self.__pin = pin
#
#     def show(self):
#         if self.__pin==12345:
#             return  f"{self._balance} {self.__pin}"
#
#
# myobj=BankAccount(10000,00000 )
#
# print(myobj.show())
#
# b)
# class Employee:
#     company = "SoftClub"
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(f"{self.name} {self.company}")
#     @classmethod
#     def change_company_name(cls, new_company_name):
#         cls.company = new_company_name
#
# obj1 = Employee("Tavhid")
# obj1.show()
# obj2 = Employee("Sunnatullo")
# obj2.change_company_name("NEW Company")
# obj2.show()


# Task4:
# class Animal:
#     def __init__(self):
#         pass
#     def speak(self):
#         print("Animal Sound!")
#
# class Dog(Animal):
#     def speak(self):
#         print("vuf vuf vuff")
#
# class Puppy(Dog):
#     def speak(self):
#         print("zzzzzzzzzzzz")
#
#
# animal = Animal()
# dog = Dog()
# puppy = Puppy()
#
# animal.speak()
# dog.speak()
# puppy.speak()


# Task5:
# from datetime import datetime
#
# class Person:
#     def __init__(self, name, country, birth_date):
#         self.name = name
#         self._country = country
#         self._birth_date = birth_date
#         self._current = datetime.now()
#
#     def show(self):
#         print(f"age is: {self._current.year - self._birth_date}")
#
# obj1 = Person("Tavhid", "Tajikistan", 2000)
# obj1.show()


# Task7:
# def test(a:str):
#     cnt=0
#     for i in a:
#         if i.isupper():
#             cnt+=1
#     if cnt>0 and cnt<len(a):
#         return "mixed"
#     elif cnt == len(a):
#         return "upper"
#     else:
#         return "lower"


# Task9:
# num = 9
#
# for i in range(num//2+1):
#     for j in range(i+1):
#         print( i+1, end=" ")
#     print()
# for i in range(num//2,0,-1):
#     for j in range(i):
#         print( i, end=" ")
#     print()



# Task10:
# class IceCream:
#     def __init__(self, flavor, num_sprinkles):
#         self.flavor = flavor
#         self.num_sprinkles = num_sprinkles
#         self.my_dict = {
#             "Plain":0,
#             "Vanilla":5,
#             "ChocolateChip":5,
#             "Strawberry": 10,
#             "Chocolate": 10
#         }
#         self.res = 0
#
#     def show(self):
#         print(f"{self.my_dict[self.flavor] + self.num_sprinkles}")
#
# person1 = IceCream("Chocolate", 13)
#
# person1.show()


# Task6:
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#
#     def show(self):
#         return f'"{self.category}", {self.year}, "{self.winner}"'
#
# person = Nobel("Peace", 2005, "Muhammad Sodikov")
# print(person.show())