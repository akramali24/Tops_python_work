'''Write a Python script to concatenate following dictionaries to create a new one.'''

dict1 = {1:"apple",2:"orange"}

dict2 = {3:"cherry",4:"mango"}

new_dict = dict1
new_dict.update(dict2)
print(new_dict)