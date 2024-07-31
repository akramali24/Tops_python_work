'''Write a Python program to remove an empty tuple(s) from a list of tuples.'''

my_tuple=[(1,2,3,4),(),(5,6),(),(7,8)]

list1=[]
for empty_tuple in my_tuple:
    if len(empty_tuple)==0:
        my_tuple.remove(empty_tuple)
print(my_tuple)        