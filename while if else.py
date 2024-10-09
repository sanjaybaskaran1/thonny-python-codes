"""print only odd numbers between 1 to 50"""
num = 0
while num <= 50:
    if (num%2) == 0:
        num +=1
        continue
    else:
        print(num, end=' ')
        num+=1
        