# li=[1,2,3,4]
# li_new=[]
# for ele in li :
#     li_new.append(ele**2)
# print(li_new)
#
# li_even_square=[ele**2 for ele in li if ele%2==0]
# print(li_even_square)

# li = [ele**2 for ele in range(10) if ele%3 ==0]
# print(li)

# li = [[ i*j for j in range(4)] for i in range(3)]
# print(li)
#
# def rowWiseSum(arr):
#     list = []
#     for row in arr:
#         sum = 0
#         for ele in row:
#             sum = sum + ele
#         list.append(sum)
#     return list
#
# str=input().split()
# m, n =[[int(i) for i in input().strip().split("")]for i in range ("")]
#
# l = [[int(i) for i in input().strip().split()]for i in range()]
# arr = [[l[(j * n) + i] for i in range(n)] for j in range(m)]
# l = rowWiseSum(arr)
# print(*l)

#
# from sys import stdin
#
#
# def spiralPrint(mat, nRows, mCols):
#     loop = nRows
#     if loop % 2 != 0:
#         loop += 1
#     for i in range(loop // 2):
#         for j in range(i, mCols - i):
#             print(mat[i][j], end=" ")
#         for k in range(1 + i, nRows - i):
#             print(mat[k][j], end=" ")
#         for l in range(mCols - 2 - i, -1 + i, -1):
#             print(mat[k][l], end=" ")
#         for p in range(nRows - 2 - i, 0 + i, -1):
#             print(mat[p][l], end=" ")
#
#
# # Taking Input Using Fast I/O
# def take2DInput():
#     li = stdin.readline().rstrip().split(" ")
#     nRows = int(li[0])
#     mCols = int(li[1])
#
#     if nRows == 0:
#         return list(), 0, 0
#
#     mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
#     return mat, nRows, mCols
#
#
# # main
# t = int(stdin.readline().rstrip())
#
# while t > 0:
#     mat, nRows, mCols = take2DInput()
#     spiralPrint(mat, nRows, mCols)
#     print()
#
#     t -= 1
# li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# for j in range(4):
#     for ele in li:
#         print(ele[j],end = "")
# a = {1:2,'list':[1,2],3:5}
# a.pop('list')
# a['list'] = [3,5]
# print(a['list'])\

# s = {1,2,3,5,4,2,3,1}
# print(len(s),end= "")
# s.add(4)
# s.add(3)
# print(len(s))


# s = {}
# s.add(4)
# s.add(4)
# print(len(s))