class college:
    name = "mgr"
    
    def display(self):
        return"hello",self.name
        
mgr = college()
print(mgr)
print(mgr.name)
print(mgr.display())


"""print(mgr.display()) calls the display method on the mgr instance.
Inside this method, self refers to mgr, so self.name is "mgr".
The method returns a tuple ("hello", "mgr").
So, self is used to access the instance's attributes and methods from within the class.
Without self, the method would not know which instance's attributes it should work with."""