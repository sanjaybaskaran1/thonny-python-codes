state = {"tamilnadu":[1,2,3,4,5],
         "mumbai":[6,7,8,9,10],
         "delhi":[11,12,13,14,15],
         "karnataka":[16,17,18,19,20]}

iterr = iter(state.values())
print(iterr)
value1 = next(iterr)
print(value1)
value2 = next(iterr)
print(value2)
value3 = next(iterr)
print(value3)
value4 = next(iterr)
print(value4)
sum1,sum2,sum3,sum4=(0,0,0,0)
for j1 in value1:
    sum1 +=j1
for j2 in value2:
    sum2 +=j2
for j3 in value3:
    sum3 +=j3
for j4 in value4:
    sum4 +=j4
print("sum1=",sum1,"sum2=",sum2,"sum3=",sum3,"sum4=",sum4)
