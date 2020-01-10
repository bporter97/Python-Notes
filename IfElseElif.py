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
