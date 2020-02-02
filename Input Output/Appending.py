import webbrowser
# Opening a file in append mode, causes the data that is input to be
# at the end of the file. This is similar to the write mode, however writing
# to a file instead of appending it, will cause the previous contents of the file
# to be erased or replaced with the new data.
# To append to a text file, use 'a' instead of 'r' or 'w'

# This opens your web browser to python's built-in functions page so you can learn more about
# said functions.
webbrowser.open('https://docs.python.org/3/library/functions.html#open')

# Here we create a new file with the contents: "Hello, this is a new file"
# using the with open functions and assign the file a name, with the editing type 'w' for write.
# From there we append the file with the contents of the endContents variable.
# Last but not least, we check that we can read the file again once it has been appended

newContents = ["Hello, this is a new file"]

with open('new.txt', 'w') as newfile:
    for newC in newContents:
        print(newC, file=newfile)

endContents = ["This is the file now that it has been appended "]

with open('new.txt', 'a') as newfile:
    for endC in endContents:
        print(endC, file=newfile)

with open('new.txt', 'r') as newfile:
    for line in newfile:
        print(line, end='')

