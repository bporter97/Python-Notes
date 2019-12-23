# Use "\n" to split strings across multiple lines

splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# Use "\t" to tab contents of a string
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# Backslashes can also be used to escape special characters such as quotes and double quotes
print('The pet shop owner said "No, no, \'e\'s uh,....he\'s resting".')
# Or
print("The pet shop owner said \"No, no, 'e's uh,... he's resting\".")

# You can also use triple quotes for strings

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".  """)


# Additionally, you can split strings across multiple lines by writing them over multiple lines
# This split can be cancelled by using the the backslash (\) as well.
anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)

# If you would like to include backslashes in your strings you will need to either
# prefix the string with an r, or put an addtional backslash in the string.
print('Example without r or \\\\: ', "C:Users\timbulchalka\notes.txt")

print("Examples with prefixing string with r or adding double backslashes")
# The 'r' stands for raw string
print("C:Users\\timbulchalka\\notes.txt")
print(r"C:Users\timbulchalka\notes.txt")

input()


