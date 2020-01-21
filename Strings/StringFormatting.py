for i in range(1, 13):
	print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
	

#We can clean up the above line of code by inputting a colon followed by applying a field width
print(" ")
print("Clean Version")
for i in range(1, 13):
	print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))


#The Lines of code below left-align the output using the less-than sign <
print(" ")
print("Cleaner")
for i in range(1, 13):
	print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

#We can also center the output of the code by using a ^ instead of a <
print(" ")
print("Mr. Clean")
for i in range(1, 13):
	print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

# We can specify the amount of numbers shown after a decimal by using the the f function, preceeded by a number
print("")
print("Floating point format")	
print("The value of pi is {0:12}".format(22/7))
print("The value of pi is {0:12f}".format(22/7))
print("The value of pi is {0:12.50f}".format(22/7))
print("The value of pi is {0:52.50f}".format(22/7))
print("The value of pi is {0:62.50f}".format(22/7))
print("The value of pi is {0:72.50f}".format(22/7))
#The maximum precision that can be defined in python is between 51 and 53 numbers
#I know that the value of pi is off. Don't harp on me


#Another way of formating numbers and strings is using "f" as represented below.
print(f"Pi is approximately {22 / 7:12.50f}")

input()
