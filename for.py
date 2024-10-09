my_dictionary = {
    "students":["krishna","joo","joshef","aaron"],
    "marks" : [99,100,33,44]
    }

print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())
print()

for key in my_dictionary:
    print(f"key={key}, value={my_dictionary[key]}")
print()   
    
for key,value in my_dictionary.items():
    print(f"key={key}, value={value}")