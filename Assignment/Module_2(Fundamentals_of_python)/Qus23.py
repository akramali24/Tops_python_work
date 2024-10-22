'''Write a Python function to insert a string in the middle of a string. '''


def string_middle(original, insert):
    middle = len(original) // 2 
    result = original[:middle] +  insert + original[middle:]
    
    return result

string = "HelloWorld"
insert1 = "Python"
print(string_middle(string, insert1)) 
