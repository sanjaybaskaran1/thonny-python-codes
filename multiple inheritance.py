"""multiple inheritance, 1 CHILD INHERIT FROM MULTIPLE PARENT CLASS"""

"""PARENT1"""
class COLLEGE:
    def college_name(self):
        print("student belongs to mgr college")
        
"""PARENT2"""       
class COURSE:
    def course_name(self):
        print("student is studying BTech")

"""PARENT3"""       
class DEPARTMENT:
    def department_name(self):
        print("student belongs to Information Technology department")
        
"""1 CHILD INHERIT PARENT1, PARENT2, PARENT3"""
class STUDENT(COLLEGE,COURSE,DEPARTMENT):
    def student_name(self):
        print("The student name is sanjay")
        
student = STUDENT()
student.student_name()
student.college_name()
student.course_name()
student.department_name()

        
        