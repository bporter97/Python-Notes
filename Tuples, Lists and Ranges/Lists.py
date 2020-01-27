# Lists in python can be a sequence of strings as well
# as a sequence of lists.
# Lists are defined by use of square brackets []

# The code block below prints out each game on a seperate line, along with an
# append to the list; which adds Halo 5 as the fifth game
haloGames_list = ["Halo 1", "Halo 2", "Halo 3", "Halo 4"]
haloGames_list.append("Halo 5")
for game in haloGames_list:
    print("This game is " + game)

# Lists can also be concatenated, meaning the lists can be added together
# Here we take the haloGames_list and add in all the games that did not
# follow Master Chief
moreHalo_List = ["Halo Reach", "Halo 3 ODST", "Halo Wars"]
allHalo = haloGames_list + moreHalo_List
# allHalo.sort() # You can sort lists as well using the .sort() function however,
# the function does not return numbers. If you need to return the values, use the
# sorted() function with the variable you want to return inside the parenthesis
print(allHalo)

# The .count function is used in this code block to count the periods in the ip
# address that was entered by the user
ip = input("Please enter an IP address:")
print(ip.count("."))

# even = [2, 4, 6, 8]
# # another_even = even
# # another_even.sort(reverse=True)
# # print(even)
