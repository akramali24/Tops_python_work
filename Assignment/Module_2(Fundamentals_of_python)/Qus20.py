'''Write a Python function that takes a list of words and returns the length 
of the longest one. '''

def word_longest_length(words):
    long_length=0
    for word in words:
        word_length=len(word)
        if word_length > long_length:
            long_length=word_length
    return long_length
list=['banana','mango','cherry','watermelon']
print("this a longestword in this list :",word_longest_length(list))
