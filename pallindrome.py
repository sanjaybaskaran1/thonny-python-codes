name = input("Enter a word: ")
reverse = ""
for n in name:
    reverse = n+reverse
if name == reverse:
    print(f"{name} is, pallindrome")
else:
    print(f"{name} is, not pallindrome")
    
