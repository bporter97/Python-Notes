import os
os.chdir(r'C:\Users\porter.blake\github\Python-Notes\files') # set to your path
f = input("Enter File Name: ")
fname = open(f, 'r')

def strip_func(file): # function strip_func defined
    for line in file :  
        strip = line.strip() # function is an algorithm designed to strip the newlines from the file and then 
        print(strip.upper()) # print them out in all uppercase format

strip_func(fname) #function strip_func is called
