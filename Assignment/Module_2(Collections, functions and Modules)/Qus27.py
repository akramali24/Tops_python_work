'''Write a Python program to find the repeated items of a tuple.'''

my_tuple=(1,2,3,4,5,4,2,1,1,3,2,6)
dict_repeated={}
for num in my_tuple:
    if num in dict_repeated:
        dict_repeated[num]+=1
    else:
        dict_repeated[num]=1

for num ,count  in dict_repeated.items():
    print(num,":",count)
