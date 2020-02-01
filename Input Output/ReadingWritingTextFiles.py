# Python can read and write to files.
# To do this, assign a variable and use the open command as seen below, followed by the path of the file that you want
# to read.
# From there, insert a comma after the path, followed by an r for read.
# After you are done reading/writing/editing a file, be sure to close it using the
# ".close" method

# The code block below opens a sample text file that contains the Jabberwocky poem by Lewis Carroll,
# and then, using the 'r' command, reads the file.
# From there, a for loop is instantiated to print out each line of the file that contains the string "jabberwock".
# After the for loop is executed, the file is then closed using the ".close" method.

# jabber = open("G:\My Drive\Python\Masterclass\IO\sample.txt",'r')

# If you include the file you want to read in the project folder, you should be able to
# just input the name, instead of the full path.

jabber = open("sample.txt", 'r')

for line in jabber:
    if "jabberwock" in line.lower():
        print(line)

jabber.close()

# Additionally, you can use the "with" function in python to open txt files.
# The "with" function will open and close files
# The code block below executes a with function with the sample.txt file and uses the as
# function to assign the txt file the variable of jabber.
# It then prints out all lines of the file that contain the JAB string

with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

# The code block below reads the file and uses a while statement to execute a print() method for every line
# in the sample file.

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

# You can also convert the contents of a file into a list, tuple, dictionary etc...

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

print('==' * 40)

print("WRITING TO A TEXT FILE")

# Writing to a text file is similar to reading one, except that you use a 'w' in place of the 'r'
# The code block below takes a list of states and reads them into the new states.txt file that was
# created using the "with" function

states = ['Texas', 'California', 'Nevada', 'New york', "Colorado"]

with open("states.txt", 'w') as states_file:
    for state in states:
        print(state, file=states_file)

# The additional code block is to verify that we can indeed read the file after it was created.

states2 = []
with open("states.txt", 'r') as states_file2:
    for state in states_file2:
        states2.append(state)

print(states2)
for state in states2:
    print(state)

# Additionally, you can use the ".strip" method to strip out contents at the beginning or end of a file or string

print("Texas".strip('T'))
