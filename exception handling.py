"""EXCEPTION HANDLING"""

"""1)TRY BLOCK"""
"""TRY A BLOCK OF CODE AND CHECK FOR EXCEPTION"""

"""2)CATCH BLOCK"""
"""DO THIS IF THERE WAS AN EXCEPTION"""

"""3)ELSE BLOCK"""
"""DO THIS IF THERE WAS NO EXCEPTION"""

"""4)FINALLY BLOCK """
"""DO THIS NO MATTER WHAT HAPPENS"""

try:
    file = open(file="a_file.txt")
except FileNotFoundError as error_message:
    # print(f"the {error_message} file not found")
    file = open(file="a_file.txt", mode="w")
    file.write("something something ")
else:
    file.read()
finally:
    file.close()
    print("file has been closed")