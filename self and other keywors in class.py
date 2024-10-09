class JAANU:
    def __init__(jaanu,name):
        jaanu.name = name
    def concat(jaanu,lavanya):
        print(jaanu.name + lavanya.name)
        print(lavanya.age)

class LAVANYA:
    def __init__(self):
        self.name = "Lavanya"
        self.age = 20
lavanya = LAVANYA()
  
        
jaanu = JAANU(name="Jaanu")
print(jaanu.__dict__)
jaanu.concat(lavanya=lavanya)