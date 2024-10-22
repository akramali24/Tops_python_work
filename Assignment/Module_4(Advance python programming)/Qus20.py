'''Write python program that user to enter only odd numbers, else will raise an exception.'''

try:
    num = int(input("enter the number : "))

    if num % 2 == 0 :
        raise ValueError (f"Invaild number!, {num} is not an odd number.")    
    print(f"this is an odd number : {num}")  

    
except ValueError as ve:
    print(ve)    

