'''Write a Python program to write a list to a file.'''


my_list = ["Python is also a high-level,","interpreted programming language known for its readability and versatility."]
with open('dome1.txt',"w") as file :
    for line in my_list:
        file.write(line)
    print(file)    

file.close()