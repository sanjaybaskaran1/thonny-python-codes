def student_details():
    student_id = 1
    student_name = "sanjay"
    student_grade = "A"
    
    return {
             "id":student_id,
             "name":student_name,
             "grade":student_grade
            }


print(student_details())

student1 = student_details().items()
print(student1)

for key,value in student1:
    print("key =",key, ",value = ",value)
