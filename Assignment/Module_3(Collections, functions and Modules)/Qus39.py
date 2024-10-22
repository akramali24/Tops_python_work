'''Write a Python script to merge two Python dictionaries '''


dict1={1:"a",2:'b',3:'c'}
dict2={4:'d',5:'e',6:'c'}

merge= dict1.copy()
merge.update(dict2)
print(merge)
