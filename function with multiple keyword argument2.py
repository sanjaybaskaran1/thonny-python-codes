def calc(n, **numbers):
  add = n + numbers["add"]
  mul = n * numbers["multiply"]
  print(n)
  print("addition =", add)
  print("multiplication =",mul)

calc(n=2, add=5, multiply=2)


