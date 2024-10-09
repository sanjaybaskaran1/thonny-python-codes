class student:
    def __init__(self,stud_name, stud_age,stud_course):
        self.name = stud_name
        self.age = stud_age
        self.course = stud_course
            
        
    
student1 = student("sanjay",18,"btech")
print(student1.name,student1.age,student1.course)