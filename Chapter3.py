# Conditional Statements & Loops

a = input("Enter a number: ")
b = input("Enter another number: ")
c = input('Enter Operator: ')

if c == "+":
    print(int(a) + int(b))
elif c == "-":
    print(int(a) - int(b))
elif c == "*":
    print(int(a) * int(b))
elif c == "/":
    print(int(a) / int(b))
else:
    print("Invalid Operator")

# While Loop

a = 1
while a <= 10:
    print(a)
    a += 1

# For Loop

for i in range(1, 11):
    print(i)

# Write a program to print table of a number
a = int(input("Enter a number: "))
for i in range(1, 11):
    print(a , 'x', i, '=', a * i)

for i in range(0,4):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()