#task4:
num = int(input("enter a number: --> "))

my_prime_list = []

for i in range(1,num+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt == 2:
            my_prime_list.append(i)

print(my_prime_list)



#task5:
n = int(input("enter a number: --> "))

my_list = []
for i in range(1,n+1):
    my_list.append(i)
new_list = []
for i in my_list[::-1]:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt != 2:
        my_list.remove(i)

print(my_list)
print(len(my_list))


#task1:
import asyncio
import time

async def test(message):
    await asyncio.sleep(2)
    print(message)


async def main():
    await test("main function finished")

asyncio.run(main())


#task2:
import asyncio
import time

async def test(message):
    await asyncio.sleep(2)
    print(message)


async def main():
    await test("task completed")

asyncio.run(main())


#task6:
def sum_all_numbers(*args, **kwargs):
    args_sum = sum(arg for arg in args)
    kwargs_sum = sum(value for value in kwargs.values())
    return f"sum of *args: {args_sum}\nsum of **kwargs: {kwargs_sum}"


#task9:
students = [
    ("Muhammad", 85),
    ("Abdullo", 92),
    ("Sunnat", 78),
    ("Tavhid", 95)
]
maxx = ["for_test",-999999]

for student in students:
    if student[1] > maxx[1]:
        maxx = student
print(maxx)

new_list = sorted(students)
print(new_list)

