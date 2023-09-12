# Числа Фибоначчи с помощью цикла while

number = int(input("Enter the number above 1: "))
value = 1
value1 = 0
value2 = 1
counter = 2
while value < number:
    value = value1 + value2
    value1 = value2
    value2 = value
    counter += 1
if value == number: print(f"The number in row is {counter}")
else: print(-1)