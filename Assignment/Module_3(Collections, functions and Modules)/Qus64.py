'''Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.'''

decimal_num=[2.354,2.365,2.556,2.536,2.646,2.045]

max_num=decimal_num[0]
min_num=decimal_num[0]

for num in decimal_num:
    if num > max_num:
        max_num=num
    elif num < min_num:
        min_num=num
print(f"maximum decimal number is {max_num}")
print(f"minimum decimal number is {min_num}")