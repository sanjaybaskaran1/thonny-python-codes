state = {"tamilnadu":[1,2,3,4,5],
         "mumbai":[6,7,8,9,10],
         "delhi":[11,12,13,14,15],
         "karnataka":[16,17,18,19,20]}

iterr = iter(state.values())
print(iterr) 

i=0
values_list = []

while i< len(state): 
    values_list.append(next(iterr)) 
    i += 1
print(values_list)


for i in values_list:
    print("sum of",i,"=",sum(i))
   
   
    