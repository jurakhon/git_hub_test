# Question1:
# from datetime import datetime, timedelta
#
# datetime.now() ##vakti hoziraro nishon medihad.
# datetime.strptime() ##vaktro az string megirad.
# datetime.strftime()
# timedelta ##baroi ruz yo hafta kafo yoki pesh kardan istifoda mebarem.
#
# num = random.random() #yagon chiz kabul namekuna dar daruni qavs
#
# rand_int = random.randint(1,100) #daruni qavs interval doda metonem.
# x = random.sample
# y = random.choices(weights=, k=)


Question2:
with open("my_file.txt", "r") as my_new_file: ## masalan
    a
    a+
    w
    r
    my_new_file.readlines()
    my_new_file.read()
    my_new_file.writelines()
    my_new_file.

Question3:
github baroi istoriya yo versiyaro kayd kardan. va kodhoro ba github monda baroi hama kodhoro ivaz kardan istifoda burda meshavad. baroi kollabaratsiya va yak proyektro hamakasa kor kardan istifoda mebarand bisyori vakt.


# Task1:
# my_list = [1, 1, 2, 3, 4, 4, 5, 1]
#
#
# element = input("Enter an element:---> ")
# i = int(input("Index:---> "))
#
# my_list.insert(i, element)
#
# print(my_list)


# Task2:
# from datetime import datetime, date, time, timedelta
#
# current_time = datetime.now()
# timexxx = timedelta(days=2)
# days_2_before = current_time - timexxx
# print(f"current time is: {current_time.date()}")
# print(f"2 days before is: {days_2_before.date()}")
# days_2_after = current_time + timexxx
# print(f"2 days after is: {days_2_after.date()}")


# Task3:
# from datetime import datetime, date, time, timedelta
# given_date = "17.02.2024"
#
# res = datetime.strptime(given_date,"%d.%m.%Y")
# print(res)
#
# timexxx = timedelta(days=5)
# days_5_before = res.date() - timexxx
#
# print(f"{days_5_before}")


# Task4:
# def sum_of_vowels(a):
#     values = {
#         'a': 4,
#         'e': 3,
#         'i': 1,
#         'o': 0,
#         'u': 0
#     }
#
#     sum = 0
#     for i in a:
#         low_char = i.lower()
#         if low_char in values:
#             sum += values[low_char]
#     return sum


# Task5:
#
# with open("my_file.txt", "r") as my_new_file:
#     num = int(input("enter line number:--->"))
#     res = my_new_file.readlines()
#     print(res[num-1])


# Task6:
# rep = input("Enter a word: ")
#
# with open('my_file.txt', 'r') as my_new_file:
#     line = my_new_file.readlines()
#
# for i in range(0, len(line), 2):
#     line[i] = rep + '\n'
#
# with open('my_file.txt', 'w') as my_new_file:
#     my_new_file.writelines(line)
#
#
# print(line)


# Task7:
# import random
#
# my_list = ["!","%","#","&","@","^","(","*",")",1,2,3,4,5,6,7,8,9,0,"h","v","x","b","o","l","g","r","u","i","m","Q","W","R","T","Y","A","S","D","F","G","N","Z"]
#
# n = int(input("enter your desired password length:--->"))
# my_pass = random.choices(my_list,k=n)
#
# print(*my_pass,sep="")


# Task8:
# num = int(input())
#
# my_dict = {}
# for i in range(1, num+1):
#     my_dict[i] = i**2
# print(my_dict)

# Task9:
# def char_appears(a, b):
#     words = a.lower().split()
#     b = b.lower()
#     return [i.count(b) for i in words]


