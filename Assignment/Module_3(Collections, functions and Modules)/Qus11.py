'''Write a Python function that takes a list and returns a new list with unique 
elements of the first list. '''


def unique_element_list(nums):
    unique_element=[]
    for num in nums:
        if num not in unique_element:
            unique_element.append(num)
    return unique_element

list_num=[1,2,3,4,2,5,4,4,5,5,6,7,8,7,4,2,9,6,5]

element=unique_element_list(list_num)
print(f"This is new list with unique element :{element}")