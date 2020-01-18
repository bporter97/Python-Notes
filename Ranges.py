# Ranges are a built in type in python 3
print(range(100))
my_list = list(range(10))
print(my_list)

# Ranges can be used to build lists
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))
print(even)
print(odd)

# Ranges don't support all operations that can be performed on sequences
# Multiplication and concatenation or appending are not supported

# The code below shows you behind the scenes of ranges:
# The .index function shows you the position of a character within
# the range whereas inputting brackets with a number shows the character
# at said index.
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))

# When ranges have the same output, they are considered equivalent.
# Example below: even though both ranges are different, they output the same
# set of numbers
for i in range(0, 5, 2):
    print(i)
for i in range(0, 6, 2):
    print(i)
print(range(0, 5, 2) == (range(0, 6, 2)))

# When slicing backwards with ranges, the start and stop values must be reversed
# for the ranges to work the way they are intended.
# Example: The first range will not print out anything because it has already reached
# the end of the range (zero). Whereas the second range will print something out

for i in range(0, 100, -5):
    print(i)
for i in range(100, 0, -5):
    print(i)

# Stepping backwards in a string can also be used for printing strings
# in reverse:
backwardsString = "gnirts sdrawkcab a si sihT"
print(backwardsString[::-1])


