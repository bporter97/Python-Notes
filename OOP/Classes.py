# Objects in python can be considered instances of a class, and Classes can be considered blueprints
# for a said object.

# Exampe: x = 10, so therefore, the variable x is an instance/object of the integer class, that has a value of 10
# whereas something like y = "Hello" would me the variable y is an instance/object of the
# string class, with the value of "Hello".
# Classes allow us to have built in functionality in python.

# import turtle

# Below, a constructor from the turtle class, creates an object of the turtle class named hair.
# The constructor that is called is the .Turtle() method

# a method is going to be anything that you are calling on an object itself.

# hair = turtle.Turtle()



# a function is created with the "def" keyword and takes an object and applies an operation to it

# Methods and functions are essentially the same thing, meaing they both return a value, however a method is
# passed ON an object, whereas a function needs to have an object passed through it.


def func(x):
    return x +1
 
print(func(5))

# CREATING CLASSWS AND OBJECTS

# To create a class, start off with the "class" command followed by the name of the class you would
# like to create.

class Dog(object):
    def __init__(self, name): # This is the constructor method: "__init__" needs to be in most classes. This will automatically start when you initialize an object. If you were not to include this in your classes, then you would have to use __init__ on the object itself when you initialize it
        self.name = name        # attributes are like variables, except they belong to a certain object. In this case, the self keyword stands for the instace your calling. 
                                # So if a initialize an object of type dog thats called "brandy", then "self" in this case, would be referring to "brandy" of type "Dog"
        
        # Methods, like functions, are created with the "def" keyword. Except, you have to call them using an object.
        
    def speak(self):
        print("Hi I am", self.name)

brandy = Dog("Brandy")

brandy.speak() # Here we call the speak method from class Dog, which in turn, will print out "Hi I am Brandy"

input()










