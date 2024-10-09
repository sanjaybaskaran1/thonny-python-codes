def add(x,y):
    return (x+y)
print(add(x=10,y=5))

"""lambda function is otherwise called as anonymous function"""
print((lambda x,y,z : x+y+z)(x=20,y=20,z=20))

"""lambda function stored inside variable"""
sum = (lambda x,y,z : x+y+z)
print(sum(x=10,y=10,z=10))