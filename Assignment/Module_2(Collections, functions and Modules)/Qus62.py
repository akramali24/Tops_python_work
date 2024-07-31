'''Write a Python program to calculate surface volume and area of a cylinder '''

r=float(input("Enter the radius : "))
h=float(input("Enter the height : "))
pi=3.14
cricle=2*(pi*r*r)
rectangle=2*pi*r*h

Area= cricle + rectangle

print(f"area of a cylinder : {Area}")