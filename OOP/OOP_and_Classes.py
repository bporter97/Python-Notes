# Imperative programming involves providing a computer
# with a series of instruction that are in a defined order.

# Object Oriented programming combines data and the processes
# that work on that data into objects. This is also known as encapsulation

# Object Oriented programming makes use of imperative programming
# in the methods that object use to manipulate their data.

# Performing tasks using an OOP approach uses less code.
# "Python Supports multiple programming paradigms, including object-oriented,
# imperative, and fucntional programming or procedural styles."
# https://en.wikipedia.org/wiki/Python_(programming_language)

import webbrowser

webbrowser.open('https://en.wikipedia.org/wiki/Python_(programming_language)')
# In this case, 'webbrowser' is an object, and '.open' is a method thats
# included in the webbrowser object

a = 12
b = 4
print(a + b)
print(a.__add__(b)) # _add_ is the method here


# A class can be considered a template from which objects can be created
class Kettle(object):

    def __init__(self, make, price): # initializes class using the __init__Constructor
        self.make = make
        self.price = price
        self.on = False

# The code below creates an instance of the kettle class called "kenwood"
# Each instance of the kettle class has its own name and price
# Each make and price instace of the kettle class can be accessed by
# using dot notation.
# if i wanted to access the price of the kenwood instance I would put
# kenwood.price.

kenwood = Kettle("Kenwood", 8.99) # Here, an object of type Kettle is initialized and called "Kenwood" with a price of 8.99
print(kenwood.make)               # This happened because the make and price attributes were initialized in the def __init__ code bock
print(kenwood.price)

kenwood.price = 12.75 # Adjusting price
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price,
                                        hamilton.make, hamilton.price))

# When a variable is band to an instance of a class is is considered
# a data attribute. In the case above, make and price in the Kettle
# class are attributes.
