class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        print(f"Student object has been created.")

    def __del__(self):
        print(f"Student object has been deleted.")
        
# Creating an instance of the Student class
std1 = Student("Sanjay", 18, "BTech")
print(' ')

print("student name = ", std1.name)
print("student age = ", std1.age)
print("student course = ", std1.course),print(' ')
# Deleting the instance explicitly
del std1

# Note: The destructor will also be called automatically
# when the program exits and the object is garbage collected.


"""In Python, a destructor is a special method called __del__,
which is called when an object is about to be destroyed.
The __del__ method allows you to define cleanup actions that should be taken when an object is garbage collected."""
