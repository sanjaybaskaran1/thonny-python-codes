num = int(input("Enter a number: "))
string = str(num)
len1 = len(string)
print("len=",len1)

amstrong=0
for i in string:
    i = int(i)
    power = i**len1
    amstrong += power
    print(i, power)
print("amstrong = ", amstrong)


if amstrong == num:
    print(f"{num}, is amstrong number")
else:
    print(f"{num}, is not amstrong number")