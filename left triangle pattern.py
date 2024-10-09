n=5

"""increment star pattern"""
for row in range(n):
    for column in range(row+1):
        print("*", end='')
    print()

print(' ') #create a new line

"""decremental star pattern"""
for row in range(n):
    for j in range(n-row):
        print("*", end='')
    print()
    

    
