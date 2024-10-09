"""40 to 80 sum of multiples of 6, count of multiples of 11"""

multiple_of_6 = []
multiple_of_11 = []

for num in range(40, 81):
    if num % 6 == 0:
        multiple_of_6.append(num)
    elif num % 11 == 0:
        multiple_of_11.append(num)
sum=0     
for i in multiple_of_6:
    sum += i
print(multiple_of_6)
print(sum)

count=0
for i in multiple_of_11:
    count += 1
print(multiple_of_11)
print(count)