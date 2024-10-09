dictionary = {"apple": 100,
              "banana": 50,
              "orange": 25,
              "mango":45}
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items()), print(" ")

#accesing key and value inside the iter_obj
iter_obj1 = iter(dictionary.items())
print(iter_obj1)
for key, value in iter_obj1:
    print(f"key = {key}, value = {value}")
print(" ")

#accessing keys inside the iter_obj
iter_obj2 = iter(dictionary)
print(iter_obj2)
for key in iter_obj2:
    print("key = ",key, ", value = ",dictionary[key])
print()

#accessing keys inside the iter_obj
iter_obj3 = iter(dictionary.keys())
print(iter_obj3)
for key in iter_obj3:
    print("key = ",key, ", value = ",dictionary[key])
print()

#accessing values inside the iter_obj
iter_obj4 = iter(dictionary.values())
print(iter_obj4)
for value in iter_obj4:
    print("value = ",value)
print()

#accesing key and value inside the iter_obj
iter_obj5 = iter(dictionary.items())
print(iter_obj5)
for i in range(0, len(dictionary)):
    key, value = next(iter_obj5)
    print(f"key = {key}, value = {value}")
