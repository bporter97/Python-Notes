# Sets in python are unordered (meaning they will display differently each time the code is executed)
# and do not contain duplicates, similar to a dictionary in python
# Items in sets are NOT access with a key in a set.
# Elements in a set must be immutable

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)
print("=" * 40)

# The code below shows how a set is defined; in this case, we passed a list that contains
# lion, tiger, panther and elephant into the "set" constructor.
# it does not include keys like a dictionary and
# can also be defined by the 'set' function.

wild_animals = set(['lion', 'tiger', 'panther', 'elephant'])

for animal in wild_animals:
    print(animal)

# To add elements to a set, use the '.add' method.
# The code block below adds "Horse" to the farm_animals set and the wild_animals set.
farm_animals.add("horse")
wild_animals.add("horse")

print("=" * 40)

print(farm_animals)

print("=" * 40)

print(wild_animals)


print("=" * 40)

# To create an empty set, you MUST use the "set" function
empty_set= set()

# You can also pass ranges into sets and any other type of object as well.
# However you will have to use the "set" constructor instead of the curly braces as seen
# by the first example.
firstRange = set(range(0, 101, 10))


# The ".union" method allows entries from sets to be merged together.
# The only thing is, it will only merge the entries that are not included in the
# parent set.

# The code block below show how two sets are defined, and the length of the sets that are defined.
# It then uses the .union method to integrate the squares set into the even set.

even = set(range(0, 40, 2))
print(even)
print(len(even))

print("=" * 40)

squares_tuple = {4, 6, 9, 16, 25}
squares = set(squares_tuple)
print(squares)
print(len(squares))

print("=" * 40)

# This merges the squares set with the even set, therefore
# The entries, 9 and 25 are added into the even set and will be displayed
# in the programs output

print(even.union(squares)) # "squares" is being merged into "even"
print(len(even.union(squares)))

print()

print("Compare the first and last sets to to see how they differ in length and in their contents")

print("=" * 40)

# The ".intersection" method merges the entries that the two sets have in common.
# The code block below shows how the intersection method is called.

# all outputs will be the same

print(even.intersection(squares))
print(even & squares) # An ampersand can be used to call the .intersection method
print(squares.intersection(even))
print(squares & even)

print("=" * 40)

# Use the sorted function to print out the set's contents in order
evenTwo = set(range(0, 40, 2))
print(sorted(even))
squares_tupleTwo = (4, 6, 9, 16, 25)
squaresTwo = set(squares_tupleTwo)
print(sorted(squaresTwo))

print()

# Use the ".difference" (or use a "-") method to subtract sets from each other
# The code block below uses the .difference method to find the difference between the two sets
# In other words, it looks between the two set's items to see which items from the "squaresTwo"
# set is not a part of the "evenTwo" set as well.

print("even minus squares")
print(sorted(evenTwo.difference(squaresTwo)))
print(sorted(evenTwo - squaresTwo))

print("=" * 40)

# Use the ".difference_update" function to display the set without the difference
print(sorted(evenTwo))
print(squaresTwo)
evenTwo.difference_update(squaresTwo)
print(sorted(even))

print("=" * 40)

# To remove entries in the set, you can use the ".discard" and ".remove" methods
# Both methods remove entries, however the ".remove" method will throw an error
# if the entry that was input is not valid.

# The Code block below throws and error because 8 was already removed from the list.
# So trying to remove it again with the ".remove" method causes an error to be thrown.
# This can be bypassed by replacing the .remove method for item 4 with .discard

squaresTwo.discard(4)
squaresTwo.remove(16)
squaresTwo.discard(8)
print(squaresTwo)
squaresTwo.remove(4)

# The error that is thrown when the .remove method is called can also be circumvented
# by checking for the value with an if function.

if 8 in squaresTwo:
    squaresTwo.remove(8)

