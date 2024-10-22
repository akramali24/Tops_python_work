'''Write a Python program to read a file line by line and store it into a list'''

my_list=[]

file= open("dome.txt", "r")

for line in file.readlines():
    my_list.append(line.strip())
print(my_list)    

file.close()