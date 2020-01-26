name = input("Please Enter Your Name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# This code demonstrates the program flow control with if and else statements.
# It takes the variables input by the user in the code above and determines if they are grater than or
# equal to a value set by the programmer.

if age >= 21:
    print("You are old enough to drink")
    print("Have fun!")
else:
    print("Please come back in {0} years".format(18 - age))

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 7:
    print("Please guess higher")
    guess = int(input())
    if guess == 7:
        print("Good job! You guessed correctly!")
    else:
        print("Sorry, your guess was wrong")
elif guess > 7:
    print("Please guess lower")
    guess = int(input())
    if guess == 7:
        print("Good job! You guess correctly!")
    else:
        print("Sorry, your guess was wrong")
else:
    print("You got it first time")


#The Code below demonstrates the use of the "and" function to supply two arguments to the if statement.
# Parenthesis can be used to separate variables of the statement to make it easier to read, but they are not needed.
age2 = int(input("How Old are you?"))
if (age2 >= 16) and (age2 <= 65):
    print("Have a good day at work")
# You can also clean up the above code more by using only one equation:
if 16 <= age2 <= 65:
    print("Have a good day at work")

# If statements can also use an "or" function to test between two variables:
# In the code below, "or" is used to test and see if either expression is true. If found true, the if statement
# will print "Enjoy your free time"
if (age2 < 16) or (age2 > 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# Python has True and False boolean values, where True is a value of 1, and False is a value of 0
# The Statement below uses the "not" function to print the opposite of the boolean values
print(not False)
print(not True)
# The not function essentially reverses any statement/output.
