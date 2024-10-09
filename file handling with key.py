"""file handling with keyword --> efficient and brilliant way to handle the file"""

with open("C:\\Users\\Sanjay\\OneDrive\\Desktop\\new_file.txt","w") as file1:
    file1.write("\nWrite mode over writes")
    file1.write("\nthe existing text in the file")
    file1.write("\nHello guys")
    file1.write("\nThis is new text")

    
with open("C:\\Users\\Sanjay\\OneDrive\\Desktop\\new_file.txt","r") as file1:
    print(file1.read())
