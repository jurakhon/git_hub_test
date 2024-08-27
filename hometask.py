# Task1:
#
# def potatoes(a:str):
#     print(a.count("potato"))
#
# potatoes(input())


# Task2:
# def sum_of_elements(a:list):
#
#     sum = 0
#     for i in a:
#         if i>5:
#             sum+=i
#     print(sum)
#
# my_list = input()
# my_list = [int(x) for x in my_list.split()]
# sum_of_elements(my_list)


# Task3:
# def shuttering_f(a:str):
#
#     print(a[0]+a[1]+(".")*3+" "+a[0]+a[1]+(".")*3+" "+a,end="")
#     print("?")
#
# shuttering_f(input())


# Task4:
# def discount(a:int,b:int):
#     res = ((100 - b)*a)/100
#     print(res)
#
# discount(int(input()), int(input()))

# Task5:
# def end_corona(a:int,b:int,c:int):
#     z=a-b
#     res=c//z
#     print(res+1)
#
# end_corona(int(input()),int(input()), int(input()))

# Task6:
# def number_split(a):
#     left = a // 2
#     right = a - left
#     print( [left, right])
#
# number_split(int(input()))



# Task7:
# def check_equals(list1, list2):
#     if len(list1) != len(list2):
#         return False
#
#     for i in range(len(list1)):
#         if list1[i] != list2[i]:
#             return False
#
#     return True



# Task8:
# def no_first_char(a: str):
#     print(a[1:len(a)])
#
#
# no_first_char(input())


# Task9:
# def harmonic(a):
#     sum = 0
#     for i in range(1, a+1):
#         sum += 1/i
#     return sum



# Task10:
# def reverse(a):
#     return a[::-1].swapcase()