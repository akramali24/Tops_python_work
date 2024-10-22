'''Write a Python program to count the frequency of words in a file.'''

file = open('dome.txt','r')
lines = file.read().split()

print(len(lines))

file.close()