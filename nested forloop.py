for i in range(0, 5):
    for j in range(i,5):
        print("*", end='')
    for k in range(0,i-1):
        print(" ", end='')
    for j in range(0,i+1):
        print("*", end='')
    print()