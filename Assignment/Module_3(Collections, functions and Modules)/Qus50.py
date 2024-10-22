'''Write a Python function to check whether a number is perfect or not. '''


def perfect_num():
    num = int(input("Enter the number : "))

    result = 0

    for i in range(1,num):
        if (num % i) == 0 :
            result=result+i
    if result == num :
        print (f"{num} is perfect number.")
    else:
        print(f"{num} is not perfect number.")
        
perfect_num()