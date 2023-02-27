# star traingular pattern
n=int(input())
i=1
p = 1
while i<=n :
    j=1

    while j<=i :
        print('*', end="")
        j=j+1
        p = p + 1

    print()
    i=i+1


# n=int(input())
# i=1
# while i<=n :
#     j=1
#     while j<=i :
#         print(1, end="")
#         j=j+1
#     print()
#     i=i+1



# square pattern


# n=int(input())
# i=1
# while i<=n :
#     j=1
#     while j<=n :
#         print(i, end="")
#         j=j+1
#     print()
#     i=i+1
#
# n=int(input())
# i=1
# while i<=n :
#     j=1
#     while j<=n :
#         print(n-j+1, end="")
#         j=j+1
#     print()
#     i=i+1
#triangular pattern
# n=int(input())
# i=1
# while i<=n :
#     j=1
#     while j<=i :
#         print(j, end="")
#         j=j+1
#     print()
#     i=i+1
#
n=int(input())
i=1
while i<=n :
    j=1
    p=i
    while j<=i :
        print(p, end="")
        j=j+1
        p=p+1
    print()
    i=i+1
#
# n=int(input())
# i=1
# p = 1
# while i<=n :
#     j=1
#
#     while j<=i :
#         print(p, end="")
#         j=j+1
#         p = p + 1
#
#     print()
#     i=i+1
###character pattern


# # print kth alphabet
# k = int(input())
# # 'A' + k - 1
# x = ord('A')
# asciiTarget = x + k - 1
# targetChar = chr(asciiTarget)
# targetChar


# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         # print jth column
#         charP = chr(ord('A') + j - 1)
#         print(charP, end='')
#         j = j + 1
#     print()
#     i = i + 1



# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     start_char = chr(ord('A') + i -1)
#     while j <= i:
#         # print jth column
#         charP = chr(ord(start_char) - j + 1)
#         print(charP, end='')
#         j = j + 1
#     print()
#     i = i + 1


# n=int(input())
# i=1
# while i<=n :
#     j=1
#     while j<=j :
#         print(j, end="")
#         j=j+1
#     print()
#     i=i+1
#
#     n = int(input())

# n = int(input())
#
# currRow = 1
# while currRow <= n:
#     currCol = currRow
#
#     while currCol >= 1:
#         print(currCol, end="")
#         currCol -= 1
#     print()
#     currRow += 1

# n=int(input())
# i=1
# print(1)
# while i<=n-1:
#     print(i,end="")
#     num_2=2
#     while num_2<=i: #no of Colums
#         print("0",end="")
#         num_2+=1
#     print(i)
#     i=i+1