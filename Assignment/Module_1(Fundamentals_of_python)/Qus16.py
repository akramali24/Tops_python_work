# Write a Python program to count the occurrences of each word in a given sentence 

string="this is is a python"
words=string.split()

word_dict={}

for  word in words:
    if word in word_dict:
        word_dict[word]+=1
    else:
        word_dict[word]=1
 
for word, count in word_dict.items():
    print(word,":",count)