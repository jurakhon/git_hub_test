

# question1:
# rekursiya takror ba ru omadan mano dorad. yak funksiyaro vizov karda value ro ivaz namuda ba joi iteration istifoda burda metonem. yane mo metonem ki valuero ivaz karda takror takror faryod kunem funksiyaro va vazifaro ijro kunem.
#
# question4:
# list comprehension yak metode meboshed ki ba yaxel vazifahoro dar daruni list comprehension ba joi iteration hal kunem. yane loop nagirifta metonem har yak elementhoro ivaz yo hal kunem. incchunin dictionary comprehensionro ham key : value kati bo vositai comprehension hal kunem.
#
# question5:
# random.random() # az 0.0 to 1.0 random rakam
# random.randrange(1, 100, 2) #start stop step doda rakami random girifta metonem.
# random.choices(k=) #weight k= doda tagabozi karda metonem.
# random.shuffle # shuffle mekunad elementhoro yane aralash karda mepartoya.
# random.randint # ba monandi randrange meboshad yagon integer megirad dilxoh.
# datetime.now() # vakti hoziraro nishon medihad.
# datetime.weekday() # az 0 to 6 az ruzi dushanbe to ruzi bozor.
# datetime.strptime() # ba string megardonad.
# datetime.strftime() # az string mexonad.
# datetime.year, month, day # sol moh, ruz ro nishon medihad.
# timedelta # az yagon vakti datetime to yagon vakti muayyan chi kadar vakt guzasht yoki meguzarad timedelta istifoda burda hisob karda metonem.
#
# question2:
# closere in zamikaniya mano dorad. mo metonem az inner ba outer return kunem va az funksiyai outer funksiyai innerro istifoda barem.
#
# question3:
# list yak container meboshad, tuple, set ham. dar daruni in containerho elementhoro soxranit karda istifoda burda metonem.
#
#
# Task1:
#
# tjs_currency = int(input("Enter the amount in TJS:"))
# rub = 8.33
# usd = 0.094
# euro = 0.084
# uz_sum = 1000
#
# print(f"TJS in Rubles: ---> {tjs_currency*rub}")
# print(f"TJS in USD: --->{tjs_currency*usd}")
# print(f"TJS in EUR: --->{tjs_currency*euro}")
# print(f"TJS in UZ_SUM: --->{tjs_currency*uz_sum}")

# Task8:
# def calculate(n):
#     res = 1
#     fact = 1
#
#     for i in range(1, n + 1):
#         fact *= i
#         res += 1 // fact
#
#     return round(res, 5)


# Task7:
# def replace(a):
#     words = a.split()
#     res = []
#     for i in words:
#         if len(i) >= 5:
#             res.append('#' * len(i))
#         else:
#             res.append(i)
#     return ' '.join(res)


# Task2:
# def my_func(a):
#     return int("".join(map(str, a)))
#
#
# lst = [11,22,33]
# res = my_func(lst)
#
# print(lst)
# print(res)



# Task3:
# def outer(a):
#     def inner(b):
#         return a + " " + b
#     return inner
#
# my_country = outer("Salom")
# res = my_country("Tajikistan")
# print(res)



# Task4:
# def min_num(a):
#     a = [int(x) for x in a.split()]
#
#
#     minn = 999999
#     for i in a:
#         if i<minn:
#             minn=i
#     return minn
#
# print(min_num(input()))



# Task10:
# s = input()
# length = len(s)
# middle = length // 2
# result = []
#
# for i in range(length):
#     if i < middle:
#         result.append(s[i])
#         result.append('(')
#     elif i == middle:
#         if length % 2 == 0:
#             result.append(s[i])
#             result.append(')')
#         else:
#             result.append(s[i])
#     else:
#         result.append(')')
#         result.append(s[i])
#
# output = ''.join(result)
# print(output)


# Task5:
# n = int(input())
#
# sum_squares = (n * (n + 1) * (2 * n + 1)) // 6
#
# print(sum_squares)