# Write a Python program to count the number of characters (character frequency) in a string.

string = "hello world"

frequency_dict={} #duplicate key is not allow

for num in string:
    frequency = string.count(num)
    frequency_dict[num]=frequency
for key,value in frequency_dict.items():
    print(key,":",value)