"""opening the file in write mode"""
file = open("C:\\Users\\Sanjay\\OneDrive\\Desktop\\new_file.txt","w")
print(file)
file.write("this is python class.")
file.write("\ni dont know python")
file.write("\ni know python")
file.close()
print(' ')

"""opening file in write mode"""
file = open("C:\\Users\\Sanjay\\OneDrive\\Desktop\\new_file.txt","r")
print(file.read())
file.close()

"""opening the file in append mode"""
file = open("C:\\Users\\Sanjay\\OneDrive\\Desktop\\new_file.txt","a")
file.write("\nappend mode will not over writes the existing text")
file.write("\nin the file so it is safer than write mode")
file.close()
print(' ')

file = open("C:\\Users\\Sanjay\\OneDrive\\Desktop\\new_file.txt","r")
print(file.read())
file.close()