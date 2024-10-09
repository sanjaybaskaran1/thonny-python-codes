"""method overriding"""
class ANIMALS:
    def sounds(self):
        print("ALL ANIMALS HAVE UNIQUE SOUNDS.")
animal = ANIMALS()
animal.sounds()

print()

class DOG(ANIMALS):
    def sounds(self):
        print("Dog maks BOW BOW sound.")
        
class CAT(ANIMALS):
    pass

dog = DOG()
dog.sounds()
print(' ')
cat = CAT()
cat.sounds()
