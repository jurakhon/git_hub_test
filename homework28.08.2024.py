# Task3:
# import random
#
# my_list = ["!","%","#","&","@","^","(","*",")",1,2,3,4,5,6,7,8,9,0,"h","v","x","b","o","l","g","r","u","i","m","Q","W","R","T","Y","A","S","D","F","G","N","Z"]
#
# n = int(input("enter your desired password length:--->"))
# my_pass = random.choices(my_list,k=n)
#
# print(*my_pass,sep="")


# Task2:
# import random
#
# array1 = [random.randint(0, 1) for i in range(6)]
# array2 = [random.randint(0, 1) for i in range(6)]
#
# print("First array:")
# print(array1)
# print("Second array:")
# print(array2)
#
#
# print("Test above two arrays are equal or not!")
# if array1 == array2:
#     print(True)
# else:
#     print(False)

# Task1:
# import random
#
# num = random.randrange(1,100)
# print(f"this is the random number: {num}")
# cnt = 0
# while True:
#     user_input = int(input("enter your guess:--->"))
#     if cnt >=5:
#         print("You lose!! Game over!!")
#         break
#
#     if user_input - num <=10:
#         print("too close")
#         cnt+=1
#     if user_input == num:
#         print("You Winnnnn!!!!!!")
#         break
#     elif user_input - num >=11:
#         print("too high")
#         cnt+=1
#     elif user_input - num <=-11:
#         print("too low")
#         cnt+=1
#     elif user_input - num >=-10:
#         print("too close")
#         cnt+=1


# Task4:
# import random
#
#
# while True:
#     comp = random.randrange(1,3)
#     user = int(input("Select your move (1 for Rocks,2 for Paper, 3 for Scissors):---->"))
#     if comp==user:
#         print("It's a tie!")
#         break
#     if comp==1 and user==3:
#         print("You Lose")
#         break
#     elif comp==1 and user==2:
#         print("You Win!!!")
#         break
#     elif comp==2 and user==1:
#         print("You Lose")
#         break
#     elif comp==2 and user==3:
#         print("You win!!")
#         break
#     elif comp==3 and user==1:
#         print("You win!!")
#         break
#     elif comp==3 and user==2:
#         print("You lose")
#         break