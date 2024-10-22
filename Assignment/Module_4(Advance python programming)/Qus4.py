'''Write a Python program to read first n lines of a file.'''

file=open("dome.txt", "r")
first_line=file.readline()
print(first_line)
file.close()