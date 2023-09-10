# To comment use #
#Basic python types
#Also you can use """ above and below the code
"""
Basic
python
types
"""

int_value = 5
float_value = 2.53267896
bool_value = True
value = None
string_value = "something"
dynamic_type = 4

#Use print() to output smth

print(int_value, float_value, round(float_value, 2), bool_value, value, string_value)
print("dynamic_type", type(dynamic_type), "=", dynamic_type)

dynamic_type = "new value"

print("dynamic_type", type(dynamic_type), "=", dynamic_type)

#Interpolation
print(f"{int_value} - {float_value} - {bool_value} - {value} - {string_value}")
print(f"Int_value = {int_value} etc.")

print("{} - {} - {} - {} - {}".format(int_value, float_value, bool_value, value, string_value))

#Use input() to input smth

#print("Enter the value:")
#input_value = input()
#print(f"input_value {type(input_value)} = {input_value}")

another_value = 5.363
print(another_value)
another_int = int(another_value)
print(another_int)

print("Enter the integer value:")
int_number = int(input())

