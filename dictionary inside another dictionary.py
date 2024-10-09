
"""how to access the keys and values of dictionary which is inside another dictionary"""
showroom ={
             "chennai":{"suzuki":700000,"ford":2000000,"bmw":5000000},
             "delhi":{"suzuki":700000,"ford":2000000,"bmw":5000000}
          }

print(showroom.keys())
print(showroom["chennai"])

print(showroom["chennai"].keys())
print(showroom["chennai"]["ford"])