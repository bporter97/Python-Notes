# When printing strings and numbers, it would often be convenient to display both values
# using a single call to print. For example, we may want to print a description of what a value is, before the value itself.
# Numbers can't be concatenated with strings using +.
# Instead we can use the str function in python to couerce our numbers into a string.

age = 22
print("I am " + str(age) + " years old")

# The example below is another method of combining strings with numbers.
print("I am {0} years old".format(age))

#Another Example:
days = 31
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(days, "Jan", "March", "May", "Jul", "Aug", "Oct", "Dec"))

# The example above provides format for using replacement fields. Replacement fields are defined by
# curly braces {} containing the number of a position, much like arrays. These position numbers are then defined
# by the .format() function, which will contain data inside the paranthesis, much like the line of code above.


input() 