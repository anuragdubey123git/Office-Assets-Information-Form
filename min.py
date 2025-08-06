# l=[2,5,1,3,6,9,18]
# #  0 1 2 3 4 5 6
# min=l[0]
# for i in l:
#     if i < min:
#         min=i
# print(min)

def my_min(l):
    minimum=l[0]
    for i in l:
        if i<minimum:
            minimum=i
    return minimum
l=list(map(int,input("enter numbers with comma:-").split(',')))
print("Minimum numer is:-",my_min(l))

#
# min=l[0]
# for i in l:
#     if i > min:
#         min=i
# print(min)
#
#
# def min(list):
#     min=list[0]
#     for val in min:
#         if val<min:
#             min=val
#     return min
# list=map(list,input().split())
# print(min(list))
