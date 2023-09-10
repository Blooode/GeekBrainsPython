# Some boolean magic

a = 5 >= 2
b = 5 < 2
c = 2 > 1 and 5 < 3
d = 2 >= 1 and 5 > 3
e = 2 > 1 or 5 <= 3
f = not 2 == 1
g = not 2 > 1
print(a, b, c, d, e, f, g)

# Conditions If-else
# if condition:
#   code
# elif condition:
#   code
# else:
#   code

#elif = else if

username = None #input("Enter the name: ")
if username == "Denis":
    print("It's Denis!")
elif username == "Mary":
    print("It's Mary!")
elif username == "Richard" or username == "richard":
    print("Hello, Richard!")
else:
    print(f"Hi, {username}!")

# Cycles While
# while condition:
#   code

value = 10
while value != 1:
    value -= 1
    print(value)

# About While-else
# Else are working if it's not "break" in while-part

number = 20
while number != 1:
    #if number == 15:
    #    break
    number -= 1
    print(number)
else:
    print(f"Final number is {number}")

# Indexes in string

word = "SomEthiNg"
print(word[0], word[1], word[2], word[3], word[4], word[5], word[6], word[7], word[8])
# Mirroring of the word
print(word[-1], word[-2], word[-3], word[-4], word[-5], word[-6], word[-7], word[-8], word[-9])
# Printing all
print(word, word[:])
# 3 parametres: [1:2:3]. 1 is starting index, 2 is finishing index (not included), 3 is a shift
print(word[:4], word[4:], word[3:6], word[::2], word[9::-2])

# Cycle "for" as "foreach" from C#

for char in word:
    print(char)

#Cycle range(1, 2, 3) where 1 is start of range, 2 is finish of range, 3 is a shift
values = range(5)
for value in values:
    print(value)

values = range(5, 10)
for value in values:
    print(value)

values = range(10, 3, -2)
for value in values:
    print(value)

# Methods of strings

# Searching and output true or false
print("thi" in word)
# Output of the length
print(len(word))
# Output of lower-case word
print(word.lower())
# Output of upper-case word
print(word.upper())
# Output with replacing one part to the other part
print(word.replace("SomE", "AnY"))