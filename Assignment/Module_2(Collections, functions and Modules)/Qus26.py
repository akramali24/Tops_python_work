'''Write a Python program to replace last value of tuples in a list.'''

tuple_in_list=[(1,2,3,4,5,6,7,8,9)]
replace_value=10

for num in tuple_in_list:
    convert_in_list=list(num)
    convert_in_list[8]=replace_value
    convert_in_tuple=tuple(convert_in_list)
    print(convert_in_tuple)