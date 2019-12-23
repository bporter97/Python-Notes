# Strings are one of pythons sequence data types
# 		  01234567890123
parrot = "Norwegian Blue"

print(parrot)

# Use brackets in an expression to print a specific character from a string
# Ex: parrot[3] will print the "w" character since the character count starts at 0
# with N in "Norwegian Blue" being 0, O being 1, R being 2 and W being 3
print(parrot[3])

# Mini Challenge:
# Add some code ot the program, so that it prints out "we win"
# Each character should appear on a separate line.
# The program should get the characters from the parrot string, using indexing.
# The w is already printed out, you just need to print the remaining 5 characters.
# With the text that is already being printed, the final output from the program should be:
# Norwegian Blue
# w
# e
#
# w
# i
# n

print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

# You can index backwards as well by using a "-" symbol
print()

print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])



# Slicing
# The expression below is asking python to start at position 0 and slice all the way
# up to, but not including position 6
# Last character is not included in slice
print(parrot[0:6]) #Norweg
print(parrot[0:5]) #we
print(parrot[0:9]) #Norwegian
print(parrot[:9]) # Same as starting from 0

print(parrot[10:14])
#or
print(parrot[10:])
# Same rules apply for using a "-" sign as well
print(parrot[-4:-2])
print(parrot[-4:12])

# Using a step in a slice

print(parrot[0:6:2]) #Nre
#The slice start at index postion 0.
#it extends up to (but not including) position 6.
#We step through the sequence in steps of 2

print(parrot[0:6:3]) #Nw
# The slice starts at index position 0.
#it extends up to (but not inlcuding) position 6.
#We step through the sequence in steps of 3

number = "9,223,372,036,854,775,807"
print(number[1::4])
# Starts at position 1 and slices every 4th character
# Omitting the middle number allows the slice to go all the way through the variable


# Slicing backwards

















































input()