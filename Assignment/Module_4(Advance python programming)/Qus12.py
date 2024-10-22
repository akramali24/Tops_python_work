'''Write a Python program to copy the contents of a file to another file.'''

with open('dome.txt','r') as file:
    contents = file.read()
    
with open("dome1.txt","w") as file1:
    file1.write(contents)
    print(file1)

file.close()
file1.close()