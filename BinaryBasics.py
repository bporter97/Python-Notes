# Binary is a number system that is based on 2 digits: 0 and 1
# Binary numbers are read right to left, with a zero being false and one
# being true.
# Binary numbers values are as so: 256|128|64|32|16|8|4|2|1
# So binary number 0|0|0|0|0|0|0|1|1 is equal to the valeu of three, whereas
# number 0|1|0|0|0|0|0|1|1 is equal to 131 and 0|0|0|0|0|0|0|0|0 is equal to zero.
# The code block below prints out values and their binary equivalent.

for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))
