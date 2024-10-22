# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = 10 
b = 15
c = 44

sum = a + b + c

if a == b or b == c or c == a:
    sum = 0

print("Result is :",sum)