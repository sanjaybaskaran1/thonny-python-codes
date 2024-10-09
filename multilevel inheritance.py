"""multi level in-heritance"""

"""parent class"""
class GRAND_FATHER:
    eyes = "blue eyes"
    height = "6 - feet"
    def character(self):
        print("good man")

"""child class1 which inherit properties of parent class"""
class FATHER(GRAND_FATHER):
    lips = "pinkish"
    hair = "grey"
    
"""child class2 which inherits properties of child class1"""
"""which is already inherits the properties of parent class"""
class SON(FATHER):
    pass

son = SON()
print("grand son inherits ", son.eyes, "from his grand father")
print("grand son inherits ", son.height, "height from his grand father")
print("son inherits ", son.lips, "lips from his father")
print("son inherits ", son.hair, "hair from his father")