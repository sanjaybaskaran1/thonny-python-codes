"""single inheritance"""

class ANIMALS:
    def sounds(self):
        print("ALL ANIMALS HAVE UNIQUE SOUNDS.")
animal = ANIMALS()
animal.sounds()

print()

class DOG(ANIMALS):
    pass
dog = DOG()
dog.sounds()
