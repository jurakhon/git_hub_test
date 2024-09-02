# Task8:
# def first_last(a):
#     print(a[0]+a[-1])


# Task9:
# def is_plural(a):
#     if a[-1]=="s":
#         print(True)
#     else:
#         print(False)
#
# is_plural(input())


# Task7:
# def free_cup(a):
#
#     if a>=6:
#         b = (a//6)
#         res = a + b
#         print(res)
# free_cup(int(input()))


# Task1:
# def doubleChar(a:str):
#     res=""
#     for i in a:
#         res+=i+i
#     print(res)
# doubleChar(input())

# Task2:
# def find_word():
#
#     with open('notes.txt', 'r') as my_new_file:
#         lines = my_new_file.readlines()
#         my_list=[]
#         my_str =""
#         for i in lines:
#             my_list.append(i)
#         for i in my_list:
#             my_str = " ".join(my_list)
#         res = my_str.split()
#         print(type(res))
#         print(res)
#         cnt = 0
#         for i in res:
#             if "the" in i or "The" in i:
#                 cnt+=1
#         print(cnt)
#
# find_word()


# Task3:
# def count_word():
#
#     with open('notes.txt', 'r') as my_new_file:
#         lines = my_new_file.readlines()
#         my_list=[]
#         my_str =""
#         for i in lines:
#             my_list.append(i)
#         for i in my_list:
#             my_str = " ".join(my_list)
#         res = my_str.split()
#         print(type(res))
#         print(res)
#         cnt = 0
#         for i in res:
#             if i.endswith("e"):
#                 cnt+=1
#         print(cnt)



# Task4:
# def find_word():
#
#     with open('articles.txt', 'r') as my_new_file:
#         lines = my_new_file.readlines()
#         my_list=[]
#         my_str =""
#         for i in lines:
#             my_list.append(i)
#         for i in my_list:
#             my_str = " ".join(my_list)
#         res = my_str.split()
#         print(type(res))
#         print(res)
#         cnt_this = 0
#         cnt_these = 0
#         for i in res:
#             if i=="this" or i=="This":
#                 cnt_this+=1
#             elif i=="these" or i=="These":
#                 cnt_these+=1
#
#         print(f"'This' appeared in this txt file {cnt_this} times.")
#         print(f"'These' appeared in this txt file {cnt_these} times.")
#
# find_word()


# Task6:
#
# given_list = ["red", "green","black","white","orange"]
# # user_input = str(input())
# user_input = "ack"
# for i in given_list:
#     if user_input in i:
#         print(True)
#         break
#     else:
#         print(False)
#         break

