def num(n=None):
    if n is dict:
        n = n.keys()
    
    if n is None:
        n = []
        n.append(1)
    return n
    

print(num())
print(num(n=[1,23]))
print(num(n={1:"hii",2:"byee"}))