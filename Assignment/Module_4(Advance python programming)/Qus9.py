'''Write a Python program to count the number of lines in a text file.'''

file = open('dome.txt','r')

lines = file.readlines()
print("Number of lines is",len(lines))

file.close()