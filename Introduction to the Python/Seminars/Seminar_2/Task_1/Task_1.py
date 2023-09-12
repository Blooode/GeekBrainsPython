# Найди значение факториала с помощью цикла while

factorial = int(input("Enter the value above or iqual to zero: "))
result = 1
if factorial == 0 or factorial == 1:
    result = 1
    print(f"Result is {result}")
elif factorial > 1:
    i = 1
    while i <= factorial:
        result *= i
        i += 1
    print(f"Result is {result}")
else:
    print("Value of factorial can not be below zero!")
