letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

# Prints all letters of the alphabet backwards except for A
# This is because we used the stop value of 0 and slices
# extend up to but do not include the stop value

# CHALLENGE
# Using the letters string from the video, add some code to create the following slices.
# Create a slice that produces the characters qpo
# Slice the string to produce edcba
# Slice the string to produce the last 8 characters, in reverse order.

slice1 = letters[16:13:-1]
print(slice1)

slice2 = letters[4::-1]
print(slice2)

slice3 = letters[26:17:-1]
print(slice3)

input()