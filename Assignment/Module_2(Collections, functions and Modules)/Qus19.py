'''Write a Python program to create a tuple with different data types.'''

this_tuple=(1,2.22,"hello",True,None,[1,2,3],(4,5,8),{1,2,6},{'tomato':20})

for element in this_tuple:
    print(f"{element} Type :-{type(element)}")

