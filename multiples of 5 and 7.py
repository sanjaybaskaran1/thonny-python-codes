# 50 to 100
"""find multiples of 5 and 7 between 50 and 100"""
multiples_5_and_7 = []

for i in range(50, 100+1):
    if i%5 == 0 and i%7 ==0:
        multiples_5_and_7.append(i)
        
print(multiples_5_and_7)