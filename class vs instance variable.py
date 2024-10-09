"""TO understand {instance variable} concept
create a class to find area and circumference of a circle
--> use {pi=3.14} as a instance variable
--> and use radius as a instance variable
"""
class CIRCLE:
    def __init__(self,radius,pi):
        self.c_radius = radius
        self.pi = pi
    def circumference(self):
        print("circumference = ",2*(self.pi)*(self.c_radius))
    def area(self):
        print("area =",self.pi*(self.c_radius)**2)
circle1=CIRCLE(radius=10,pi=3.14)
circle1.circumference(),circle1.area()
circle2=CIRCLE(radius=5,pi=3.14)
circle2.circumference(),circle2.area()
print(' ')




"""TO understand {class variable} concept
create a class to find area and circumference of a circle
--> use {pi=3.14} as a class variable
--> and use radius as a instance variable
"""
class CIRCLE2:
    pi = 3.14 #class variable
    def __init__(self,radius):
        self.c_radius = radius
        
    def circumference(self):
        print("circumference = ",2*(CIRCLE2.pi)*(self.c_radius))
    def area(self):
        print("area =",(CIRCLE2.pi)*(self.c_radius)**2)
circle1=CIRCLE2(radius=10)
circle1.circumference(),circle1.area()
circle2=CIRCLE2(radius=5)
circle2.circumference(),circle2.area()

































