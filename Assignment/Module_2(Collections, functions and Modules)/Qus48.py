'''Write a Python function to calculate the factorial of a number (a 
nonnegative integer)'''


def calculate_factorial(number):
    
    factorial = 1

    if number > 1:
        for i in range(1,number + 1):
            factorial *= i 
        print(f"factorial of",number,"is",factorial)
    elif number == 0 or number == 1:
        print("factorial of 0 and 1 is all ways 1.")    
    else:
        print("Enter only positive numbers")
        
        
number = int(input("Enter number: "))        
calculate_factorial(number)