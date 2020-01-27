# Iterators are objects that represent a stream of data. It returns
# the data in the stream one at a time.
# Any object that supports iteration is called an iterable

# For loops creat iterators for you.
# The code block below prints out each character before terminating
# string = "1234567890"

# for char in string:
    # print(char)
# The code block below shows the iterator in action, using the next
# function to go through each iterator
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))

list1 = ["I", "love", "oatmeal", "and", "toast"]
n = len(list1)
new_iter = iter(list1)

# while n >= len(list1):
#     for item in list1:
#         print(next(new_iter))
#         n += 1

# Cleaner version

for i in range(0, len(list1)):
    next_item = next(new_iter)
    print(next_item)

for i in list1:
    print(i)

