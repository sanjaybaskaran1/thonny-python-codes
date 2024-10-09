
"""create a function to calculate result """
def result(s_name, s_mark):
    if s_mark > 300:
        return "pass"
    else:
        return "fail"


n = int(input("Enter number of students: "))
print(' ')
i=0
while i < n:
    name =  input("enter student name: ")
    mark =  int(input("enter student mark: "))
    student = result(s_name=name,s_mark=mark)
    print(student),print(' ')
    i+=1
    