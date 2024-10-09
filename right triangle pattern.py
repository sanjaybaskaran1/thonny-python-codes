n=5
"""space decrement and start incrtement"""
for row in range(n):
    for j in range(n-row):
        print(" ", end='')
    for column in range(row+1):
        print("*", end='')
    print()
    
print(' ')#create a new line
    
"""space increment and star decrement"""    
for row in range(n):
    for column in range(row+1):
        print(" ", end='')
    for column in range(n-row):
        print("*", end='')
    print()