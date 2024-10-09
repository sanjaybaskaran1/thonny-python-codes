"""SCENARIO ONE 
You are managing a library. You want to keep track of the
total number of books in the library and also provide a
way to add new books. Use a class method to
keep track of the total number of book"""
class library:
    """class variable"""
    Total_books = 50
    
    @classmethod
    def add_books(cls,book):
        cls.Total_books += 1
    
    @classmethod
    def books_tracker(cls):
        print("Total Books = ",cls.Total_books)
    
            
lib = library()
lib.books_tracker()
"""adding new book"""
lib.add_books(book = "harry potter")
lib.books_tracker()

            
        
        