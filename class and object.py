class Animal_sound:
    """class variables"""
    dog_name = "Bairo kutty"
    cat_name = "stuart"
    
    """instance methods"""
    def dog(self):
        return(f"{self.dog_name}, The dog barks Bow Bow!")
    def cat(self):
        print(f"{self.cat_name}, The cat meows")

"""creating object for the class Animal_sound"""       
animal1 = Animal_sound()
print(animal1),print(' ')

"""calling class variables"""
print("dog_name = ",animal1.dog_name)
print("cat_name = ",animal1.cat_name),print(' ')

"""calling instance methods"""
dog = animal1.dog()
print(dog)
animal1.cat()