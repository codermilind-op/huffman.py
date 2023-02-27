# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def printLL(head):
#     while head is not None:
#         print(head.data,end=" ")
#         head = head.next
#
#
#
# node1 = Node(10)
# node2 = Node(20)
# node2.next = node1
# printLL(node2)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def printLL(head):
#     while head is not None:
#         print(head.data,end=" ")
#         head = head.next
#
#
#
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# printLL(node2)

# class Node:
#     def __init__(self, data):
#         self.data = data
# #         self.next = None
#
# def printLL(head):
#     while head is not None:
#         print(head.data,end=" ")
#         head = head.next
#
# def increment(head):
#      temp = head
#      while temp is not None:
#         temp.data +=1
#         temp = temp.next
#
#
#
# node1 = Node(10)
# node2 = Node(20)
# node1.next = node2
# increment(node1)
# printLL(node1)

#
# from sys import stdin
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def findNode(head, n):
#     curr = head
#     cnt = 0
#     while curr is not None:
#         if curr.data == n:
#             return cnt
#         cnt += 1
#         curr = curr.next
#
#     return -1
#
#
# def takeInput():
#     head = None
#     tail = None
#
#     datas = list(map(int, stdin.readline().rstrip().split(" ")))
#
#     i = 0
#     while (i < len(datas)) and (datas[i] != -1):
#         data = datas[i]
#         newNode = Node(data)
#
#         if head is None:
#             head = newNode
#             tail = newNode
#
#         else:
#             tail.next = newNode
#             tail = newNode
#
#         i += 1
#
#     return head
#
#
# def printLinkedList(head):
#     while head is not None:
#         print(head.data, end=" ")
#         head = head.next
#
#     print()
#
#
# t = int(stdin.readline().rstrip())
#
# while t > 0:
#     head = takeInput()
#     n = int(stdin.readline().rstrip())
#     print(findNode(head, n))
#
#     t -= 1


#
# takeInput()
#     print("Enter root data")
#     rootData = int(input())
#     if (rootData == -1)
#         return None
#     root = BinaryTreeNode(rootData)
#     root.left = takeInput()
#     root.right = takeInput()
#     return root




def count_Letter(word, letter):
    print("Word = ", word)
    print("Letter to count = ", letter)
    print("Number of occurrences of '", letter, " ' is = ", end="")
    count = 0


for i in word:
    if (i == letter):
        count = count + 1
    return count

x = count_Letter('INDIA', 'I')
print(x)