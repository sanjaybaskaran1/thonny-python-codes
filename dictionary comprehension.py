"""dictionary comprehension"""

student = {
      "jaanu" : "data analysis",
      "lavanya" : "data analysis",
      "joshef" : "full stack"
    }

names = [key for key in student.keys()]
course = [value for value in student.values()]
print(names)
print(course)


"""for key,value in student.items():  
    names.append(key)
    course.append(value)
print(names)
print(course)"""
    