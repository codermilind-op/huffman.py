# n=int(input())
# i=1
# while i <= n:
#     j=1
#     while j <= n-i+1:
#         print(n-i+1,end="")
#         j=j+1
#     print()
#     i=i+1
# reverse

# n = int(input())
# i = 1
# while i <= n:
#     spaces = 1
#     while spaces <= n - i:
#         print(' ', end= "")
#         spaces = spaces + 1
#     j = 1
#     while j <= i:
#         print(j, end= "")
#         j = j + 1
#     print()
#     i = i + 1

#isoceles pattern
# n = int(input())
# i = 1
# while i <= n:
#     spaces = 1
#     while spaces <= n - i:
#         print(' ', end= "")
#         spaces = spaces + 1
#     j = 1
#     p=i
#     #increase sequence
#     while j <= i:
#         print(p, end= "")
#         j = j + 1
#         p= p+1
#         # inc  sequence
#     p=i-1
#     while p>=1:
#         print(p-i+j,end="")
#         p=p-1
#     print()
#     i = i + 1

    # n = int(input())
    # i = 1
    # while i <= n: spaces = 1
    # while spaces <= n - i: print(' ', end="")
    # spaces = spaces + 1
    # j = 1
    # p = 1
    # increase sequence
    # while j <= i:
    #     print(i+j, end= "")
    #     j = j + 1
    #     p= p+1 # inc sequence
    #     p=i-1
    #     while p>=1:
    #         print(p+j-1,end="")
    #         p=p-1
    #         print() i = i + 1
    # n = int(input())
    # currRow = 1
    # while currRow <= n:
    #     spaces = 1
    #     while spaces <= n - currRow:
    #         print(" ", end="")
    #         spaces += 1
    #     currCol = 1
    #     valToPrint = currRow
    #     while currCol <= currRow:
    #         print(valToPrint, end="")
    #         valToPrint += 1
    #         currCol += 1
    #     currCol = 1
    #     valToPrint = 2 * currRow - 2
    #     while currCol <= currRow - 1:
    #         print(valToPrint, end="")
    #         valToPrint -= 1
    #         currCol += 1
    #     print()
    #     currRow += 1
    #
    #
    #

    #
    #
    #
    #
# n=int(input())
# firstHalf=(n+1)//2
# secHalf=(n)//2
#
# #First Half
# currRow=1
# while currRow<=firstHalf:
#     spaces=1
#     while spaces<=(firstHalf-currRow):
#         print(' ',end="")
#         spaces+=1
#     currcol=1
#     while currcol<=(2*currRow)-1:
#         print("*",end="")
#         currcol+=1
#     print()
#     currRow+=1
#
# #Secound Half
# currRow=secHalf
# while currRow>=1:
#     spaces=1
#     while spaces<=(secHalf-currRow+1):
#         print(" ",end="")
#         spaces+=1
#     currcol=1
#     while currcol<=(2*currRow)-1:
#         print("*",end="")
#         currcol+=1
#     print()
#     currRow-=1


# n=int(input())
# totalspace=n*2-2
# row=1
# while(row<=n):
#     column=1
#     while column<=row:
#         print(column,end='')
#         column=column+1
#     space=1
#     while space<=totalspace:
#         print(' ',end="")
#         space+=1
#     totalspace-=2
#     column=row
#     while column>0:
#         print(column,end='')
#         column-=1
#     row+=1
#     print()
#
#     n = int(input())
#     num = 1
#     gap = n - 1
#     for j in range(1, n + 1):
#         num = j
#         for i in range(1, gap + 1):
#             print(" ", end="")
#         gap = gap - 1
#
#         for i in range(1, j + 1):
#             print(num, end="")
#             num -= 1
#         num = 2
#         for i in range(1, j):
#             print(num, end="")
#             num += 1
#
#         print()
n = int(input())
i = 1
n1 = (n - 1) / 2
n = (n + 1) / 2
while i <= n:
    spaces = 2
    while spaces <= i:
        print(" ", end="")
        spaces += 1
    star = 1
    while star <= i:
        print("* ", end="")
        star += 1
    print("")
    i = i + 1

i = 1
g = 0
while i <= n1:
    num_1 = n1 - 1
    while num_1 >= i:
        print(" ", end="")
        num_1 -= 1

    num_1 = n1 - 1
    while num_1 >= g:
        print("* ", end="")
        num_1 -= 1
    print()
    i = i + 1
    g = g + 1
