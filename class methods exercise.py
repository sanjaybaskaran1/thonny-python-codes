"""exercise on methods inside the class"""
class STUDENTS:
    def __init__(self,name,mark):
        self.s_mark = mark
        self.s_name = name
    
    def result(self):
        if self.s_mark > 300:
            return "pass"
        else:
            return "fail"

s1 = STUDENTS("sanjay",250)
s2 = STUDENTS("janani",490)
s3 = STUDENTS("kutty",390)
s4 = STUDENTS("bairoo",460)

s_list = [s1,s2,s3,s4]
passed_students = []
failed_students = []
result_dict = {}

for obj in s_list:
    if (obj.result()) == "pass":
        passed_students.append(obj.s_name)
        result_dict[obj.s_name] = obj.result()
    else:
        failed_students.append(obj.s_name)
        result_dict[obj.s_name] = obj.result()
print(passed_students)
print(failed_students)
print(result_dict)
    
        