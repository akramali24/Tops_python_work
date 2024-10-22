'''Write a Python program to combine two dictionary adding values for 
common keys. 
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400} 
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}). '''



d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}

add_dict={}

for key in d1:
    if key in d2:
        add_dict[key]=d1[key]+d2[key]
    else:
        add_dict[key]=d1[key]

for key in d2:
    if key not in d1:
        add_dict[key]=d2[key]  
print(add_dict)

