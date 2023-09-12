import random

watermelon_amount = int(input("Enter the number of watermelons: "))
minimal = 1
maximal = 10
min_weight = maximal
max_weight = minimal
for i in range(watermelon_amount):
    now_weight = random.randint(minimal, maximal)
    print(now_weight)
    if now_weight < min_weight: min_weight = now_weight
    if now_weight > max_weight: max_weight = now_weight
print(f"Minimal weight is {min_weight}", f"Maximal weight is {max_weight}", sep = "\n")
