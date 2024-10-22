# Write python program that swap two number with temp variable and without temp variable.

# with the temp variable:-
print("-----with the temp variable-----")
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

temp = a  
a = b     
b = temp  

print("Swapping the first number (a)",a)
print("Swapping the second number (b)",b)

#without the temp variable:-

print("-----without the temp variable-----")
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

a = a + b
b = a - b
a = a - b

print("Swapping the first number (a)",a)
print("Swapping the second number (b)",b)