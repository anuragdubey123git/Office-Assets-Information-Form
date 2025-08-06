# l=[2,3,7,8,10]
# for i in l:
#     if i%2==0:
#       print(i,"is even")
#     else:
#       print(i,"is odd")
# print(type(l))
from importlib.metadata import unique_everseen

# year=[2001,2002,2003,2004]
# for i in year:
#     if i%4==0:
#         print(i,"is leap year")
#     else:
#         print(i,"is not a leap year")


# l=[4,5,6,1]
# print(max(l),"is max number")
# print(min(l),"is min number")


# l1=[3,4,4,3,2,1,2]
# unique=set(list(l1))
# print(unique)
# print(type(unique))


l1=[3,4,4,3,2,1,2,1,8]
unique=[x for x in l1 if l1.count(x)==1]
print(unique)

