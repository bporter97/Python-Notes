# String Operators

#Python 3 has 5 sequence types built in:
# The string type
# list 
# tuple
# range
# bytes and bytearray

# What is a sequence?

# a sequence is defined as an ordered set of items.
# For example, the string "hello world contains 11 items, and each item is a chracter.
# A list is also a sequence type. For example, here's a python list of things you might need when buying a new computer:
# ["Computer", "monitor", "keyboard", "mouse", "mouse mat"]
# That list conatins 5 items, each of which is a string.
# in other words, the example was a sequence where each item is also a sequence
# Be sure to fully understand indexing, since it is very important when dealing with sequences.

# Because a sequence is ordered, we can use indexes to acces indevidivual items in the sequence.

computer_parts = ["Computer", "monitor", "keyboard", "mouse", "mouse mat"]
print(computer_parts[1]) # Prints out "Monitor"

# That is also a sequence that we can index into as well
print(computer_parts[1][0]) # Prints out the letter "m"

# Everything that you can do with the str sequence type can also be done with the other sequence types.
# One exception though, not all sequence types can be concatenated or multiplied. range is an example.

# Sequence operators

string1 = "he's"
string2 = "probably"
string3 = "pining"
string4 = "for the"
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5) # The plus is not necessary when concatenating string literals in python

print("he's " "probably " "pining " "for the " "fjords")

# Strings can also be multiplied

print("Hello " * 5) # Prints hello 5 times

# Lists and tuples can also be multiplied
# Order of Operations is also applied when multiplying strings

# Checking for values in varaiables
today = "friday"
print("day" in today) 	#true
print("fri" in today) 	#true
print("thur" in today) 	#false
print("parrot" in "fjord")#false









# String Replacement Fields.





input()
