# task1:
# from datetime import datetime, date, time, timedelta
#
# def halloween(a):
#
#     res = datetime.strptime(a, "%Y/%m/%d")
#     month = res.month
#     day = res.day
#     if month==10 and day==31:
#         print("Bonfire toffee")
#     else:
#         print("toffee")
#
# halloween(input("Enter date in the following format:--->2013/10/31"))


# Task3:
# from datetime import datetime, date, time, timedelta
#
# def after_months(a,b:int)
#
#     new_year = datetime.strptime(a,"%Y")
#     res = b//12
#     print(res+new_year.year)

# Task4:
# from datetime import datetime
#
#
# def converter(a):
#     res = datetime.strptime(a,"%d/%M/%Y")
#     new = datetime.strftime(res,"%Y%M%d")
#
#     print(new)

# Task5:
# from datetime import datetime, date, time, timedelta
#
# given_date = datetime(2020,2,25)
#
# res = datetime.strftime(given_date, "%A %d %B %Y")
#
# print(res)

# Task2:
# def century(a):
#     if a%100==1:
#         res=(a//100)
#         print(res)
#     else:
#         res = (a//100)+1
#         print(res)
#
# century(int(input()))