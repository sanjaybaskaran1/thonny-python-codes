n = int(input("enter a number: "))
sum=1

while True:
    sum*=n
    n-=1
    if(n==0):
        break
print(sum)
        
    