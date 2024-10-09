import string

alphabets_string = string.ascii_lowercase
print(alphabets_string)
alphabets_list=[]
for i in alphabets_string:
    alphabets_list.extend([i])
print(alphabets_list)
    