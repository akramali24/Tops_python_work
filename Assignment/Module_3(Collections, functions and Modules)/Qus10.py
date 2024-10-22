''' Write a Python program to generate and print a list of first and last 5 
    elements where the values are square of numbers between 1 and 30.'''


square=[]
for num in range(1,31):
    square.append(num * num)
 
    frist_five= square[:5]
    last_five = square[-5:] 
print(frist_five+last_five)
   
