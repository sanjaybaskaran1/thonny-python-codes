def outer_function(name):
    def inner_function(name):
        print(f"hello {name}")
    return inner_function


outer = outer_function("sanjay")
print(outer)

inner = outer("sanjay")
inner