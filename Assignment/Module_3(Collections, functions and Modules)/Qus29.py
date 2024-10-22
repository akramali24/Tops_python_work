'''Write a Python program to unzip a list of tuples into individual lists.'''                                                                

list1 = [(1,2),(2,3),(4,8),(9,11)]

list2 = []
row = []
col = []

for i in list1:
    row.append(i[0])
    col.append(i[1])
    if row and col not in list2:
        list2.append(row)
        list2.append(col)
print(list2)