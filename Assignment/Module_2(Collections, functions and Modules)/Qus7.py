'''Write a Python program to remove duplicates from a list. '''


my_list=[1,2,2,3,4,5,4,6,4,5]

remove_duplicate=[]

for num in my_list:
    if num not in remove_duplicate:
        remove_duplicate.append(num)
print(f"This is unique value :{remove_duplicate}")