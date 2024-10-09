
def numbers(**karg):
    print("-----Welcome to numbers() function:-----")
    for i in karg:
        print(karg[i])
numbers(n1=10,n2=5,n3=6,n5=16)
print(' ')


def friends_names(**names):
    print("-----Welcome to friends_names() function:-----")
    for key,value in names.items():
        print(f"key = {key},  value = {value}")
friends_names(name1="lakshi",name2="jaanu",name="lavanya")
print(' ')

def sum_of_numbers(**numbers):
    print("-----Welcome to sum_of_numbers() function:-----")
    sum=0
    for num in numbers.values():
        sum+=num
    print(f"The sum of {numbers.values()} is, {sum}")
sum_of_numbers(n1=10,n2=12,n3=20)