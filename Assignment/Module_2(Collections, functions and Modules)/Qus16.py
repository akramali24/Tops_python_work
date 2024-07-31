'''Write a Python program to check whether a list contains a sub list'''


my_list=[1,2,[3,4,5,6],7,8,9]
sub_list=[3,4,5,6]

if sub_list in my_list:
    print("list contains a sub list")
else:
    print("this is not list contains a sub list")