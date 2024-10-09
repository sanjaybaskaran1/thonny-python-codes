"""find count of multiples of 11 between 10 to 100"""
multiples_of_11 = []
for i in range(10, 101):
    if i%11 == 0:
        multiples_of_11.append(i)
print(multiples_of_11)

count = 0
for i in multiples_of_11:
    count +=1
print(count)
    
        
        