def create_matrix(a,b,c):
  return [a,b,c]

new_list = create_matrix(a=[1,2,3,4],b=[5,6,7,8],c=[9,10,11,12])
print(new_list)
#returned_list = create_matrix([],[1,2,3,4],[])
#print(returned_list)
#print(returned_list[1][-1])
print(new_list[1])
print()


def matrix_new(b,a=[1,2,3,4]):
    print(a)
    print(b)
    
matrix_new(a=5,b=[5,6,7,8])