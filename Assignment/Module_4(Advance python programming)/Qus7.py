'''Write a Python program to read a file line by line store it into a variable.'''

file = open('dome.txt','r')
line = file.readlines()

for lines in line:
    print(lines.strip())
    
file.close()