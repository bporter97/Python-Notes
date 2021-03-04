import os # imports os module

os.chdir(r'P:\Python Projects\Python-Notes\files') # set's the working directory for the python script:
# Allows us to open File.txt without having to type the full file path in the open() method

ofile = open("File.txt") # To enable users to gain access to a file, we need to instantiate a variable 
# and assign it to the open() method, with the file name included in the parenthesis.
# This doesn't read the file into the program, it more or less "imports" it and allows you to call it later
# much like importing an additional python module

for i in ofile: # Python navigates files through line. This for statement with i as the loop counter
# iterates through every line in the .txt file and subsequently prints the contents;
# think of it as one giant array, where i instead of being the position in an array is the line in the file
    
    print(i) # this algorithim allows a user to search through a file line by line using the .startswith() method
    if i.startswith("Alas,") : # if a line starts with a defined set of characters, in this case: "Alas," , then the print function is called
        print("Oh no!")

# The print() function in python automatically adds a new line after it reads the line from a txt file 

rfile = ofile.read() #reads a file into memory
count = 0
for i in ofile : 
    count = count + 1

print("there are ", count, " in this excerpt")