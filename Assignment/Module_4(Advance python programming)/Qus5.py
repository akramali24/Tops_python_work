'''Write a Python program to read last n lines of a file.'''


file=open("dome.txt", "r")
lines=file.readlines()[-1:]

for line in lines:
    print(line)
file.close()