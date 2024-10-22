'''Write a Python script to sort (ascending and descending) a dictionary by value.''' 

my_dict={'apple':100,'banana':30,'mango':50,'cherry':70}

asce=[]
desc=[]

for value in my_dict.values():
    asce.append(value)
    asce.sort()
    desc.append(value)
    desc.sort(reverse=True)
print(f"Ascending order : {asce}")
print(f"Descending order : {desc}")

