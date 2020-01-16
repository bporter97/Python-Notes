# A for loop takes a range of values and assigns them one by one to a variable.
# The for loop then executes a block of code, once for each value

# This block of code prints the value of i up to 19 times
for i in range(1,20):
    print("i is now {}".format(i))

number = "1,230,987,456"
# "len" stands for length
# The code block below prints out each individual character in the number variable on a seperate line
for i in range(0, len(number)):
    if number[i] in "0123456789": # This function tests to see if the i character
        # Matches any number in the value "0123456789" an
        print(number[i])

num2 = "1,029,384,756"
remnum = ""

# The code block below extracts a character for each position in the num2 string
for char in num2:
    if char in "0123456789":
        remnum = remnum + char
newNum = int(remnum)
print("The number is {}".format(newNum))


for i in range(100):
    if (i % 7) == 0:
        print(i)
