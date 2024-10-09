"""inheritance --> hierarchical inheritance (2 or more child inherit single parent class)"""
class PARENTS:
    father_name = "Baskaran"
    mother_name = "Easwari"
    def parent_details(self):
        print(f"{self.father_name} and {self.mother_name} are the parents")
        
class CHILD1(PARENTS):
    name = "sanjay"

child1 = CHILD1()
print("The child1 name is, ",child1.name)
child1.parent_details(),print(f"of {child1.name}"),print(' ')


class CHILD2(PARENTS):
    name = "janani"

child2 = CHILD2()
print("The child2 name is, ",child2.name)
child2.parent_details(),print(f"of {child2.name}")