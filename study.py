

# x = 5
# if x < 6:
#     print("Hello")
# if x == 5:
#     print("Hi")
# else:
#     print("Hey")


# i=1
# while i<3:
#     j=0
#     while j<5:
#         j = j +1
#         if j==3:
#             continue
#         print(j,end="")
#     i = i +1
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end="")
#     for l in range(i,n+1):
#         print(l,end="")
#     print()
# for a in range(1,n):
#     for s in range(n-1-a,0,-1):
#         print(" ",end="")
#     for k in range(n-a,n+1):
#         print(k,end="")
#     print()

n = int(input())

# Upper part of diamond
for i in range(1, n-2):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

# Lower part of diamond
for i in range(n-2,0, -1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()




# h = int(input())
#
# for i in range(h):
#     print(" "*(h-i), "*"*(i*2+1))
# for i in range(h-2, -1, -1):
#     print(" "*(h-i), "*"*(i*2+1))



# rows = int(input("Enter Diamond Pattern Rows = "))
#
# print("Diamond Star Pattern")
# k = 0
# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(end = ' ')
#     while k != 2 * i - 1:
#         print('*', end = '')
#         k = k + 1
#     k = 0
#     print()
#
# k = 2
# l = 1
# for i in range(1, rows):
#     for j in range(1, k):
#         print(end = ' ')
#     k = k + 1
#     while l <= (2 * (rows - i) - 1):
#         print('*', end = '')
#         l = l + 1
#     l = 1
#     print()



n=int(input())
n1=(n//2)+1
for i in range(1,n1+1):
    for j in range(1,n1-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
n2=n-n1
for i in range(n2,0,-1):
    for j in range(1,n1-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()