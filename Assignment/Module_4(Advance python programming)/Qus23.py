'''Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle'''


class Rectangle:
    def __init__(self,length, width):
        
        self.length = length
        self.width = width
        
    def area_of_rectangle(self):
        
        area = self.length * self.width
        return area
    
r = Rectangle(2,4)

print(f"Area of rectangle is {r.area_of_rectangle()}")        