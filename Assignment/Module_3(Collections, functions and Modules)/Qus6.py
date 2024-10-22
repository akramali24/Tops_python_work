'''Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings.'''

my_list=['apea','a','aa','apple','aba','cdc','121']    

count = 0
for string in my_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
print(f"Count the first and last character are same in the my_list : {count}")