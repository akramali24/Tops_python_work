'''Write a Python program to returns sum of all divisors of a number '''


num = int(input("Enter a number : "))
result=0

for i in range(1,num+1):
    if num % i == 0:
        result+=i
print(f"Sum of all divisors of a number {result}")