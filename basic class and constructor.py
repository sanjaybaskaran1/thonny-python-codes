class student:
    def __init__(self,name,age):
        self.s_name = name
        self.s_age = age
    
    def student_detail(self):
        print("student_name = ", self.s_name)
        print("student_age = ", self.s_age)
        
student1 = student(name="sanjay",age=20)
student2 = student(name="jaanu",age=21)
student3 = student(name="kishore",age=22)
    
student1.student_detail()
print(student1.s_name, student1.s_age)
print(' ')
student2.student_detail()
student3.student_detail()