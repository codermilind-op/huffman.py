# class BinaryTreeNode:
#     def __init__(self,data):
#         self.data=data;
#         self.left=None
#         self.right=None
#
# def search(root,x):
#     if root== None:
#         return False
#     if root.data==x:
#         return True
#     elif root.data>x:
#         return search(root.left,x)
#     else :
#         return search(root.left,x)
#
# def printTreeDetailed(root):
#     if root==None:
#         return
#     print(root.data,end=":")
#     if root.left != None:
#         print("L", root.left.data, end=",")
#     if root.right != None:
#         print("R", root.right.data, end="")
#     print()
#     printTreeDetailed(root.left)
#     printTreeDetailed(root.right)
#
# import queue
# def takeTreeInputLevelWise():
#     q = queue.Queue()
#     print("Enter root")
#     rootData = int(input())
#     if rootData==-1:
#         return None
#     root=BinaryTreeNode(rootData)
#     q.put(root)
#     while(not(q.empty())):
#         current_node=q.get()
#         print("enter left child of",current_node.node)
#         leftChildData = int(input())
#         if leftChildData != -1:
#             LeftChild=BinaryTreeNode(leftChildData)
#             current_node.left=leftChild
#             q.put(leftChild)
#         print ("Enter right child of ",current_node.data)
#         rightChildData = int(input())
#         if rightChildData != -1:
#             rightChild=BinaryTreeNode(rightChildData)
#             current_node.right=rightChild
#             q.put(rightChild)
#         return root
#
# root=takeTreeInputLevelWise()
# printTreeDetailed(root)
# search(root,5)

#
#
# class BinaryTreeNode:
#     def __init__(self,data):
#         self.data=data;
#         self.left=None
#         self.right=None
#
# class BST:
#     def __init__(self):
#         self.root=None
#         self.numNodes=0
#     def printTree(self):
#         return
#     def isPresent(self,data):
#         return False
#     def insert(self,data):
#         return
#     def deleteData(self):
#         return False
#     def count(self):
#         return 0
#
# b=BST()
# b.insert(10)
# b.insert(5)
# b.insert(12)
# print(b.isPresent(10))
# print(b.isPresent(7))
# print(b.isPresent(4))
# print(b.isPresent(10))
# print(b.count())
# b.printTree()

#
# class TreeNode:
#     def __init__(self,data):
#         self.data=data;
#         self.children=list()
#
# def printTree():
#     if root==None:
#         return
#     print(root.data)
#     for child in root.children:
#         printTree(child)
#
# def printDetailedTree(root):
#     if root==None:
#         return
#
#     print(root.data,":",end="")
#     for child in root.children:
#         print(child.data,"",end="")
#     print()
#
#     for child in root.children:
#         printDetailedTree(child)
#
# n1=TreeNode(5)
# n2=TreeNode(2)
# n3= TreeNode(9)
# n4=TreeNode(8)
# n5=TreeNode(7)
# n6=TreeNode(15)
# n7=TreeNode(1)
#
# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n1.children.append(n5)
#
# n3.children.append(n6)
# n3.children.append(n7)
# printDetailedTree(n1)
#
#
# class TreeNode:
#     def __init__(self,data):
#         self.data=data;
#         self.children=list()
#
# def printTree(root):
#     if root==None:
#         return
#     printTreeDetailed(root.data,":",end="")
#     for child in root.children:
#         printTree(root.children,",",end="")
#     print()
#
#     for child in root.children:
#         printTreeDetailed(child)
#
# def takeTreeInput():
#     print('Enter Root Data')
#     rootData = int(input())
#     if rootData == -1:
#         return None
#
#     root = TreeNode(rootData)
#     print("enter number of children for",rootData)
#     childrenCount=int(input())
#     for i in range (childrenCount):
#         child=takeTreeInput()
#         root.children.append(child)
#     return root
#
# root= takeTreeInput()
# printTreeDetailed(root)
#
# import queue
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# def checkCousins(root,p,q):
#     if root==None:
#         return 0
#     return ((root.left == p and root.right == q) or
#             (root.left == q and root.right == p) or
#             checkCousins(root.left, p, q) or
#             checkCousins(root.right, p, q))
#
#
# def level(root, ptr, lev):
#
#     # Base Case
#     if root is None:
#         return 0
#     if root == ptr:
#         return lev
#
#     # Return level if Node is present in left subtree
#     l = level(root.left, ptr, lev+1)
#     if l != 0:
#         return l
#
#     # Else search in right subtree
#     return level(root.right, ptr, lev+1)
#
#
# # Returns 1 if a and b are cousins, otherwise 0
# def isCousin(root, p, q):
#
#     # 1. The two nodes should be on the same level in
#     # the binary tree
#     # The two nodes should not be siblings(means that
#     # they should not have the same parent node
#
#     if ((level(root, p, 1) == level(root, q, 1)) and
#             not (checkCousins(root, p, q))):
#         return 1
#     else:
#         return 0
#     # root.data=checkCousins(root.data)
#     # root.p=checkCousins(root.p)
#     # root.q=checkCousins(root.q)
#     # printcheckCousins(root,p,q)
#     # #Implement Your Code Here
#     # pass
#
# def buildLevelTree(levelorder):
#     index = 0
#     length = len(levelorder)
#     if length<=0 or levelorder[0]==-1:
#         return None
#     root = BinaryTreeNode(levelorder[index])
#     index += 1
#     q = queue.Queue()
#     q.put(root)
#     while not q.empty():
#         currentNode = q.get()
#         leftChild = levelorder[index]
#         index += 1
#         if leftChild != -1:
#             leftNode = BinaryTreeNode(leftChild)
#             currentNode.left =leftNode
#             q.put(leftNode)
#         rightChild = levelorder[index]
#         index += 1
#         if rightChild != -1:
#             rightNode = BinaryTreeNode(rightChild)
#             currentNode.right =rightNode
#             q.put(rightNode)
#     return root
#
# # Main
# levelOrder = [int(i) for i in input().strip().split()]
# root = buildLevelTree(levelOrder)
# p = int(input())
# q = int(input())
# ans = checkCousins(root,p,q)
# if ans is True:
#     print('true')
# else:
#     print('false')


#
# def computepay(hours,rate):
#     if hours==0:
#         return None
#     if rate == 0:
#         return None
# print("enter hours:")
# hours = float(input())
# print("enter rate:")
# rate=float(input())
# if hours<=40:
#     print("pay:", hours * rate)
#
#
# elif hours>40 :
#
#     print("pay:", 40 * rate + (hours - 40) * rate * 1.5)

    # if hours<=40:
    #     print("pay:",hours*rate)
    # elif hours>40:
    #     print("pay:",40*rate +(hours - 40)*rate*1.5)



# Score     Grade
# >= 0.9    A
# >= 0.8    B
# >= 0.7    C
# >= 0.6    D
# < 0.6


# print("enter score:")
# scr=float(input())
# if scr>=0.9:
#     print("A")
# elif scr>=0.8:
#     print("B")
# elif scr>=0.7:
#     print('C')
# elif scr >= 0.6:
#     print('D')
# elif scr < 0.6:
#     print("F")
# else :
#     print("bad")



# word = 'banana'
# count = 0
# for letter in word:
#
#     if letter == 'a':
#
#         count = count + 1
#         print(count)
# x= range(4,24,2)
# for n in x:
#     print(n,end="",)
#
# print()


# °C = [(°F-32)×5]/9


# s = int(input())
# e = int(input())
# step = int(input())
# printTable(s, e, step)

#
# def printTable(start, end, step):
#     for curr_temp in range(start, end + 1, step):
#         c = 5 / 9 * (curr_temp - 32)
#         print(curr_temp," ", int(c))
#
#
# s = int(input())
# e = int(input())
# step = int(input())
# printTable(s, e, step)
# °C = [(°F-32)×5]/9
# txt = "welcome to the jungle"
#
# x = txt.split()
#
# print(x)

# li= [int(x) for x in input().split()]
# print(li)
# 1 2 3 4 5 #User inputs the data (space separated input)
# [1,2,3,4,5] #List has integers








