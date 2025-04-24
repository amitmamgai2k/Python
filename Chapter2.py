# Strings

a = "Hello"
b = "World"

print(a + " " + b)
 # String Slicing

print(a[0:5])

# String Functions

print(a.upper())
print(a.lower())
print(a.replace("H", "J"))

# List and Tuples

a = [1, 2, 3,5,4] # List
b = (1, 2, 3) # Tuple

print(type(a), type(b))

sorted_list = sorted(a)
print(sorted_list)

# Dictinoary and sets

a = {"name": "John", "age": 30, "city": "New York"} # Dictionary
b = {"apple", "banana", "cherry"} # Set
b.add("orange")

print(type(a), type(b))

s = [8,7,12,'Harry',{1,2}]
s[4] = [3,4]
print(s)


# Practice Question

# 1. Write a program to input eight numbers from the user and display all the unique numbers once

a = [int(input()) for i in range(8)]
print(set(a))

