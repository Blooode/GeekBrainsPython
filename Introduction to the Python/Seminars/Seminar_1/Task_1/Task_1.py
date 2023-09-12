# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# Не использовать условия и циклы.

import math

speed = int(input("Enter the value of car speed (km/day): "))
distance = int(input("Enter the distance (km): "))
time = distance / speed
print(f"Count of days is {math.ceil(time)}")