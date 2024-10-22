'''Write a Python function that checks whether a passed string is 
palindrome or not'''

def string_palindrome():
    
    
    string=input("Enter the word : ")
    if string == string[::-1]:
        print(f"{string} is palindrome.")
    else :
        print(f"{string} is not palindrome.")
    
string_palindrome()