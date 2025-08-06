# number=[2,3,4,5]
# square=list(map(lambda x: x**2, number))
# print(square)
from traceback import print_exc

# number = [10,15,16,18,20,50,1,3,5,7,9,0]
# find=list(filter(lambda x: x%2 !=0,number))
# print(find)
#
number =[4,5,6,4,5,7,7,8,1,2,3,4,5]
seen=set()
duplicate=list(filter(lambda x: x in seen or seen.add(x),number))
print(duplicate)

class car:
    def __