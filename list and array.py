#adding new eliment
#insert
#append
#removing eliment
#li.remove(1)
#for removing index we use
#eg__(7,'karanb','rohan')
#li.pop(2)
#rohan will remove from list
#
#
# li=[1,2,"lion",4,"tiger"]
# # for i in range(len(li)):
# #      print(li[i])
# # for i in range (2,len(li)):
# #     print(li[i])
#
#
# # for ele in li[2:]:.......... not index
# #     print(ele)
# for ele in li[2:4]:
#     print(ele)

# li = [1,2,3,4,5]
# # for i in li[1:4]:
# #     print(i,end= "")
#
# li=[]
# for i in range(n):
#     curr=int(input())
#     li.append(curr)

# 5
# 1
# 2
# 3
# 4
# 5
# n = int(input())
# li = []
# for i in range(n):
#     li.append(input())
# print(li)
# 1 3 6 8 9
# li = [x for x in input().split()]
# print(li)
#
# def change(li):
#     li[1] = li[1] + 2
# li = [1,2,3,4,5]
# change(li)
# print(li)
# def change(li):
#     li[1] = li[1] + 2
#     li = [3,3,3,4,5]
# li = [1,2,3,4,5]
# change(li)
# print(li)

# li=int(input())
# p1,p2=1,3
# fir_ele=li.pop(pos1)
# sec_ele=li.pop(pos2-1)
# li.insert(pos1,sec_ele)
# li.insert(pos2,fir_ele)
# print(li)

# def swapPositions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list
#
#
# # Driver function
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
#
# print(swapPositions(List, pos1 - 1, pos2 - 1))
# import sys
# def takeInput():
#     n = int(sys.stdin.readline().rstrip())
#
#     if n == 0:
#         return list(), 0
#
#     arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
#     return arr, n
#
#
# # Printing the array/list
# def printList(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()
#
#
# # main
# def swapAlternate(arr,n):
#     for i in range(n):
#         print(arr[i], end="")
#     print()
#
# t = int(sys.stdin.readline().rstrip())
#
# while t > 0:
#     arr, n = takeInput()
#     if n != 0:
#         swapAlternate(arr,n)
#         printList(arr, n)
#     t -= 1

#
# # Utility function to print
# # the contents of an array
# def printArr(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ");
#
#
# # Function to update the array
# def UpdateArr(arr, n):
#     # Initialize the pointers
#     i = 0;
#     j = n - 1;
#
#     # While there are elements to swap
#     while (i < j):
#         temp = arr[i];
#         arr[i] = arr[j];
#         arr[j] = temp;
#
#         # Update the pointers
#         i += 2;
#         j -= 2;
#
#     # Print the updated array
#     printArr(arr, n);
#
#
# # Driver code
# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5, 6];
#     n = len(arr);
#
#     UpdateArr(arr, n);

