'''Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data: {'1': ['a','b'], '2': ['c','d']} 
Expected Output: ac ad bc bd'''

sample_data={'1': ['a','b'], '2': ['c','d']}

value1=sample_data['1']
value2=sample_data['2']

result=[]

for v1 in value1:
    for v2 in value2:
        result.append(v1+v2)
        
print(result)