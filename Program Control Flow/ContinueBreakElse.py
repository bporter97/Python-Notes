# In the code block below, the continue function is used.
# The way it is used is that it tests to see if there is an
# item in the shopping list by the name of syrup. If the item
# exists, then the continue will skip over printing the item.
# All other items will be printed besides syrup

breakfast_list = ["eggs", "bacon", "syrup", "oj", "pancake mix"]
for item in breakfast_list:
    if item == "syrup":
        print("We don't need " + item)
        continue
    print("Get " + item)

# Replacing "continue" with "break" will instead exit out of the for loop
# when it gets to syrup, subsequently only printing eggs and bacon

# In the code block below, a for loop is executed which searches
# for the "pancakes" item in the list. If found, it assigns pancakes
# to the "no_need" variable.

breakfast = ["eggs", "bacon", "milk", "pancakes"]
for item in breakfast:
    if item == "pancakes":
        no_need = item
        break

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

#The code block below checks if a value is assigned to the "no_need" variable.
# if the variable is found to have a value assigned to it, it then prints the following
# message.
if no_need:
    print("We don not need pancakes this morning")

# The "else" function allows a block of code to be executed if the loop
# is allowed to continue to the end
