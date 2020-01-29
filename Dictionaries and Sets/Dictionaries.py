# Dictionaries are unordered and contain keyed value pairs.
# Dictionaries aren't accessed by index, but instead are accessed by key
# The code block below shows how dictionaries are defined and how they are used

milk = {"Regular": "goes great with cookies",
        "Chocolate": "a sweet, yummy drink that can be paired with anything",
        "Strawberry": "absolutely disgusting, who drinks that??"}
# In this print statement, chocolate is the key and in turn will print "a
# sweet, yummy drink that can be paired with anything".
print(milk["Chocolate"])

# Dictionary keys HAVE to be immutable
# Here we assigned a new key called Almond with its own value to the milk
# dictionary
milk["Almond"] = "a good substitute for lactose-intolerant people"
print(milk)

# To delete keys from a dictionary:
# del milk["Strawberry"]
print(milk)
# If a key is not specified, then the entire dictionary will be removed.
# If you would to clear the dictionary of entries:
# milk.clear()

for i in range(10):
        for drink in milk:
                print(drink + " is " + milk[drink])
                print('-' * 40)

# Different ways you can sort keys; you always want to use the actual keys
# when printing them out.
# ordered_key = list(milk.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(milk.keys()))
# for f in ordered_keys:
        # print(f + "-" + milk[f])

# for f in sorted(milk.keys()):
        # print(f + '-' + milk[f])

# You can use the ".items method to print out all elements of the "Milk"
# Dictionary
# You can then produce tuples from the elements
print(milk)
print(milk.items())
print()
milk_tuple = tuple(milk.items())
print(milk_tuple)

# You can also produce dictionaries from tuples as well using the "dict"
# function
print(dict(milk_tuple))

fruit = {"orange": "Orange, citrus fruit. Main Ingredient in Orange Juice",
         "apple": "Sweet, crisp fruit. Delicious when dipped in caramel",
         "lemon": " Yellow, citrus fruit that's sour, unlike an orange",
         "grape": " Small green or purple fruit that grows on branches. Certain types can be used to make wine",
         "lime": "Like a lemon, but green. Main ingredient in margaritas",}

print(fruit)

veg = {"cabbage": "Eat on new years day to bless yourself with money throughout the year.",
       "brussel sprouts": "I think they're pretty good, idk about you",
       "spinach": "Popeye's favorite food"}

print(veg)

# You can use the .update method to update dictionaries
# The method below updates the veg directory by adding the fruit directory to it.
veg.update(fruit)
print(veg)

# You can also copy dictionaries if you would like to leave the original dictionary unchanged.
# To copy the dictionaries, use the .copy method as seen below
fruits_vegs = fruit.copy() # copies the fruit directory to a new variable (fruits_vegs)
fruits_vegs.update(veg) # Updates the fruits_vegs directory with the veg directory
print(fruits_vegs)
