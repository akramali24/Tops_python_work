'''Write a python program to find the longest words.'''

file=open("dome.txt",'r')

line=file.read().split()

longest_words=""
for word in line:
    if len(word)>len(longest_words):
        longest_words=word
print(longest_words)

file.close()