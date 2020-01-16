# While loops are used to continuously execute a block of code while a condition
# is met and stops when the condition is returned as false.


for i in range(10):
    print("i is now {}".format(i))
    i += 1

# Instead of using the above for statement to execute the block of code
# we can use a while loop instead

print('')
print("While loop starting now")
print('')

# Here we use a while loop to print out the value of i.
# This loop will continue to execute until the condition of i == 10 is met

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1
