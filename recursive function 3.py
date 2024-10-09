"""recursive function"""
"""print 10 to 1 using recursive function"""

def print_name(n):
    print(n)
    if n>1:
        print_name(n=n-1)
print_name(n=10)

"""print a name 5 times using recursive function"""
def print_name(name,n):
    if n<=5:
        print(f"n = {n}",name)
        print_name(name="jaanu",n=n+1) 
        
        
print_name(name="jaanu",n=1)
           
"""
n=10
while n>=1:
    print(n)
    n=n-1
"""
