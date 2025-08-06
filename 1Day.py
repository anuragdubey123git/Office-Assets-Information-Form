# n= int(input("Enter the row size for the pattern: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("$", end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("$",end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("A", end=" ")
#     print()

# nums=[1,2,3,4,5]
# for num in nums:
#     if num == 3:
#         break
# else:
#     print("loop completed")

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
n=int(input("enter number:"))
print(fibonacci(n))