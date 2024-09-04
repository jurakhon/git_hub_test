# Task1:
# def recursive_sum(a):
#     if len(a) == 0:
#         return 0
#     else:
#         return a[0] + recursive_sum(a[1:])
#
# my_list = [1, 2, 3, 5, 7, 3, 2, 9]
#
# res = recursive_sum(my_list)
#
# print(f"The sum of {my_list} is: {res}")


# Task2:
# def convert_to_base(n, base):
#     digits = "0123456789ABCDEF"
#     if n < base:
#         return digits[n]
#     else:
#         return convert_to_base(n // base, base) + digits[n % base]


# Task3:
# def sum_digits(n):
#
#     if n<10:
#         return n
#     else:
#         return n%10 + sum_digits(n//10)
# print(sum_digits(345))



# Task4:
# def sum_series(n):
#     if n <= 0:
#         return 0
#     return n + sum_series(n - 2)


# Task5:
# def power(a, b):
#
#     if b == 0:
#         return 1
#     else:
#         return a * power(a, b - 1)


# Task6:
# def com_divisor(a, b):
#
#     if a < b:
#         return com_divisor(b, a)
#     if b == 0:
#         return a
#     else:
#         return com_divisor(b, a % b)