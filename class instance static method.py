class STUDENT:
    
    s_course = "btech"
    s_department = "IT"
    
    def __init__(self, name, age):
        self.s_name = name
        self.s_age = age
        
    def display1(self):
        self.s_course = "bca"
        print("student name =",self.s_name)
        print("student age =",self.s_age)
        print("student course =", self.s_course)
        
    @classmethod
    def display2(cls):
        print("student department =", cls.s_department)
        
    @staticmethod
    def display3():
        print("this is static method")
        
lavanya = STUDENT(name="lavanya",age=20)
jaanu = STUDENT(name="jaanu",age=22)

lavanya.display1()
lavanya.display2()
lavanya.display3()
print(' ')
jaanu.display1()
jaanu.display2()
        

        
        
        
    

    
