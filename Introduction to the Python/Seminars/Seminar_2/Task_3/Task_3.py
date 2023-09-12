import random

days_count = int(input("Enter the amount of days: "))
count = 0
temp = 0
i = 0
while i < days_count:
    now_number = random.randint(-50, 50)
    if now_number > 0: temp += 1
    else: temp = 0
    if count < temp: count = temp
    print(now_number, end = " ")
    i += 1
print(f"The amount in the biggest row is {count}")
