'''Write a Python program to find the highest 3 values in a dictionary '''

my_dict= {'a':40,'b':30,'c':50,'d':10,'e':20}

sorted_value=sorted(my_dict.values())

print(sorted_value[-3:])