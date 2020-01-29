# An effective way of joining strings without augmented assignment is using
# the ".join" method.
# It creates the new string by taking each item in the sequence and seperating
# the items with the comma as seen on line 9. You can use this method to join
# anything to a string

myList = ['a', 'b', 'c', 'd']

stringOne = ', '.join(myList)
print(stringOne)

