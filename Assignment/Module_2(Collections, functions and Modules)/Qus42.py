'''Write a Python program to print all unique values in a dictionary.'''

my_dict = {'a': 1,'b': 2,'c': 2,'d': 3,'e': 4,'f': 4,'g': 5}

unique_value=set()

for value in my_dict.values():
        unique_value.add(value)
print(unique_value)