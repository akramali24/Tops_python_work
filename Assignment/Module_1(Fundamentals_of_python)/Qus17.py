'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string. '''

string="python"
string1="java"

if len(string) < 2 or len(string1) < 2:
    result = "Both strings must have at two characters."
else:
   
    new_string = string1[:2] + string[2:]
    new_string1 = string[:2] + string1[2:]

    result = new_string + "\n" + new_string1

print(result)
