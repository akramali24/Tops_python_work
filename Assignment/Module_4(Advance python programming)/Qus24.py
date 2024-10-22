'''Write a Python class named Circle constructed by a radius and two 
methods which will computer the area and the perimeter of a circle'''

class Circle:
    
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14
        
    def area_of_circle(self):
        
        area= self.pi * self.radius*self.radius
        return area
    
    def perimeter_of_circle(self):
        
        perimeter=2*self.pi*self.radius
        return perimeter

circle=Circle(5)

print(f"area of circle is {circle.area_of_circle()}")
print(f"perimeter of circle is {circle.perimeter_of_circle()}")