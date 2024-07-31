'''Write a Python program to get unique values from a list '''

list_num=[1,2,3,4,5,6,5,4,2,3,1]

unique_value=[]
for num in list_num:
    if num not in unique_value:
        unique_value.append(num)
print(f"To get unique values :{unique_value}")