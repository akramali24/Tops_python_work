#  Write a Python program to get the Fibonacci series of given range.

nums = int(input("Enter the number for Fibonacci series: "))

n1, n2 = 0, 1


for num in range(nums):
    if num == 0:
        print(n1)
    elif num == 1:
        print(n2)
    else:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        print(nth)
