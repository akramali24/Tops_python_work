'''Write a Python program to read a random line from a file. '''

import random

file= open("Qus1.txt", "r")

lines=file.readlines()

print(random.choice(lines))
