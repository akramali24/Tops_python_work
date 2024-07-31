'''Write a Python function that takes two lists and returns true if they have 
 at least one common member.'''


def common_member(num1,num2):
    for item in num1:
        if item in num2:
           return True
    return False

list1=[1,2,3,4,5,6]       
list2=[6,7,8,9]

print(common_member(list1,list2))