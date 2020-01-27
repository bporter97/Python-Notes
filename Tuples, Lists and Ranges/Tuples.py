# In Python, Tuples are similar to lists except that they are immutable.
# Meaning they can't be changed or appended; you would receive an error
# in doing so.

# Tuples can be defined with or without parenthesis, except for when
# syntax requires it like in the 3rd example.
# The first and third examples are tuples, signified by the square
# brackets that are printed
t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))

# Tuples can be printed over multiple lines: you can do this by adding
# square brackets containing the step in the tuple
lotrOne = "The Lord of the Rings", "The Fellowship of the Ring", 1
lotrTwo = "The Lord of the Rings", "The Two Towers", 2
lotrThree = "The Lord of the Rings", "The Return of the King", 3

print(lotrThree)
print(lotrThree[0])
print(lotrThree[1])
print(lotrThree[2])
# Lists are intended (although not enforced) to contain items of the same type.
# Tuples are intended to hold items of different types.

# Right hand sides of equations are evaluated first before the left hadn
# side of the equation is.
# Therefore you can assign a number or string to multiple variables
# or assign multiple numbers/strings to multiple variables at once.
# The example below shows how the values assigned are the same/correspond with
# their variables across the board.
a = b = c = d = 12
print(a)
print(c)
a, b, c, d = 2, 4, 6, 8
print(a)
print(c)
print(a, c)
print(b, d)
print(a, b, c, d)

# Tuples can also be "unpacked", allowing for multiple use of the items it contains
# Example: The code block below "unpacks" the tuple and assigns variables
# to the items in the tuple. The variables are then printed out using the
# print function

series, movie, movieNum = lotrTwo
print(series)
print(movie)
print("Movie No. {}".format(movieNum))

# You can also put a tuple within a tuple, and you can unpack that as well
# Tuples can also contain lists as well. The lists it contains can
# be updated.
