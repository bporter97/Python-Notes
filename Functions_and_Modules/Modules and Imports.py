# Python allows us to use modules to provide extra functionality
# to use a module, use the "import" command

import turtle
import time
# The code block below uses the turtle module to import the turtle object and it's methods into our program
# From there, we can call upon the turtle methods to move the turtle forward 150 degrees, then right 250 degrees
# and finally forward again 150 degrees

turtle.forward(150)
turtle.right(250)
turtle.forward(150)

time.sleep(4)

# You can also import methods by themselves by using the "from" command as seen below

# from turtle import forward

# doing this, you can avoid having to prefix methods with "turtle." 
# However, if you would like to use additional methods, you will need to state them
# With a comma following each subsequent one.

# You can also import ALMOST every method from a module using "from turtle import *" however
# it is not recommended. You don't know what is being imported

