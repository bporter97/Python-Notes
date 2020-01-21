print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
# You can use single or double quotes when printing strings
# However, when you start a string with one type of quote, you
# must finish the string with the same type of quote

# You can also concatanate strings using the plus sign:
print("Hello" + " world")

greeting = "Hello"
name = input("Please enter your name: ")
# The "input" function diplays the text provided to it, and then waits for user input
# to be entered. It then stores the user input into the "name" variable

print(greeting + ' ' + name)

# A variable is basically just a way to give a (meaningful name to an area of memory, into 
# which we can place certain values.

# Python variable names must begin with a laetter (either upper or lower case or an underscore_character.
# They can contain letters, numbers or underscore characters ( but cannot begin with a number).
# Python variables are case sensitive

age = 21
print(age)

# "type" stands for data type and describes the kind of information we are storing
print(type(greeting))
print(type(age))

input()
