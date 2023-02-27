# remove leaf node
# #
# class BinaryTreeNode:
#     def __init__(self,data):
#         self.data=data;
#         self.left=None
#         self.right=None
#
# def printTree(root):
#     if root==None:
#         return
#     print(root.data)
#     printTree(root.left)
#     printTree(root.right)
#
# def printTreeDetailed(root):
#     if root==None:
#         return
#     print(root.data , end=":")
#     if root.left!=None:
#         print("L",root.left.data,end=",")
#     if root.right!=None:
#         print("L",root.right.data,end="")
#     print()
#     printTreeDetailed(root.left)
#     printTreeDetailed(root.right)
#
# def treeinput():
#     rootData=int(input())
#     if rootData==-1:
#         return None
#     root=BinaryTreeNode(rootData)
#     leftTree=treeinput()
#     righttree=treeinput()
#     root.left=leftTree
#     root.right=righttree
#     return root
#
# def removeLeaves(root):
#     if root==None:
#         return None
#     if root.left==None and root.right==None:
#         return None
#     root.left=removeLeaves(root.left)
#     root.right=removeLeaves(root.right)
#     return root
#
#
# root=treeinput()
# printTreeDetailed(root)
# root=removeLeaves(root)
# printTreeDetailed(root)
#
#
#
#
# #
# #
# #
# #
# #
# # check binary tree is blanced
#
#
# class BinaryTreeNode:
#     def __init__(self,data):
#         self.data=data;
#         self.left=None
#         self.right=None
#
# def printTree(root):
#     if root==None:
#         return
#     print(root.data)
#     printTree(root.left)
#     printTree(root.right)
#
# def printTreeDetailed(root):
#     if root==None:
#         return
#     print(root.data,end=":")
#     if root.left!=None:
#         print("L",root.left.data,end=",")
#     if root.right!=None:
#         print("R",root.right.data,end="")
#     print()
#     printTreeDetailed(root.left)
#     printTreeDetailed(root.right)
#
# def treeInput():
#     rootData=int(input())
#     if rootData==-1:
#         return None
#     root=BinaryTreeNode(rootData)
#     leftTree=treeInput()
#     rightTree=treeInput()
#     root.left=leftTree
#     root.right=rightTree
#     return root
#
# def height(root):
#     if root== None:
#         return 0
#     return 1+max(height(root.left),height(root.right))
#
# def isBalanced(root):
#     if root==None:
#         return True
#     lh=height(root.left)
#     rh=height(root.right)
#     if lh-rh>1 or rh-lh>1:
#         return False
#     isLeftBlanced=isBalanced(root.left)
#     isRightBlanced=isBalanced(root.right)
#     if isLeftBlanced and isRightBlanced:
#         return True
#     else:
#         return False
#
# root=treeinput()
# printTreeDetailed(root)
# print(isBalanced(root))
# # def height(root):
# #     if root==None:
# #         return 0
# #     return 1+max(height(root.left),height(root.right))
# #
# # def isBalanced(root):
# #     if root==None:
# #         return True
# #     lh=height(root.left)
# #     rh=height(root.right)
# #     if lh-rh>1 or rh-lh>1:
# #         return False
# #     isLeftBalanced=isBalanced(root.left)
# #     isRightBalanced=isBalanced(root.right)
# #     if isLeftBalanced and isRightBalanced:
# #         return True
# #     else:
# #         return False
# #
# # root=treeInput()
# # printTreeDetailed(root)
# # print(isBalanced(root))
#
#
#
#
# #
# #
# #
# #check balanced-improve
# #
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data;
#         self.left = None
#         self.right = None
#
#
# def printTree(root):
#     if root == None:
#         return
#     print(root.data)
#     printTree(root.left)
#     printTree(root.right)
#
#
# def printTreeDetailed(root):
#     if root == None:
#         return
#     print(root.data, end=":")
#     if root.left != None:
#         print("L", root.left.data, end=",")
#     if root.right != None:
#         print("R", root.right.data, end="")
#     print()
#     printTreeDetailed(root.left)
#     printTreeDetailed(root.right)
#
#
# def treeInput():
#     rootData = int(input())
#     if rootData == -1:
#         return None
#     root = BinaryTreeNode(rootData)
#     leftTree = treeInput()
#     rightTree = treeInput()
#     root.left = leftTree
#     root.right = rightTree
#     return root
#
#
# def height(root):
#     if root == None:
#         return 0
#     return 1 + max(height(root.left), height(root.right))
#
#
# def isBalanced(root):
#     if root == None:
#         return True
#     lh = height(root.left)
#     rh = height(root.right)
#     if lh - rh > 1 or rh - lh > 1:
#         return False
#     isLeftBalanced = isBalanced(root.left)
#     isRightBalanced = isBalanced(root.right)
#     if isLeftBalanced and isRightBalanced:
#         return True
#     else:
#         return False
#
#
# def getHeightAndCheckBalanced(root):
#     if root == None:
#         return 0, True
#
#     lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
#     rh, isRightBalanced = getHeightAndCheckBalanced(root.right)
#     h = 1 + max(lh, rh)
#     if lh - rh > 1 or rh - lh > 1:
#         return h, False
#     if isLeftBalanced and isRightBalanced:
#         return h, True
#     else:
#         return h, False
#
#
# def isBalanced2(root):
#     h, isRootBalanced = getHeightAndCheckBalanced(root)
#     return isRootBalanced
#
#
# root = treeInput()
# printTreeDetailed(root)
# print(getHeightAndCheckBalanced(root))
#
# #
# #
# #
# # levelwise input binery tree
#
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data;
#         self.left = None
#         self.right = None
#
#
# def printTree(root):
#     if root == None:
#         return
#     print(root.data)
#     printTree(root.left)
#     printTree(root.right)
#
#
# def printTreeDetailed(root):
#     if root == None:
#         return
#     print(root.data, end=":")
#     if root.left != None:
#         print("L", root.left.data, end=",")
#     if root.right != None:
#         print("R", root.right.data, end="")
#     print()
#     printTreeDetailed(root.left)
#     printTreeDetailed(root.right)
#
#
# import queue
#
#
# def takeTreeInputLevelWise():
#     q = queue.Queue()
#     print("Enter root")
#     rootData = int(input())
#     if rootData == -1:
#         return None
#     root = BinaryTreeNode(rootData)
#     q.put(root)
#     while (not (q.empty())):
#         current_node = q.get()
#         print("Enter left child of", current_node.data)
#         leftChildData = int(input())
#         if leftChildData != -1:
#             leftChild = BinaryTreeNode(leftChildData)
#             current_node.left = leftChild
#             q.put(leftChild)
#
#         print("Enter right child of", current_node.data)
#         rightChildData = int(input())
#         if rightChildData != -1:
#             rightChild = BinaryTreeNode(rightChildData)
#             current_node.right = rightChild
#             q.put(rightChild)
#     return root
#
#
# root = takeTreeInputLevelWise()
# printTreeDetailed(root)



#
#
#
#buildtree using inorder and pre
#
#
#
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data;
        self.left = None
        self.right = None


def printTree(root):
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)


def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def buildTreeFromPreIn(pre, inorder):
    if len(pre) == 0:
        return None
    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInOrder = -1
    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None

    leftInorder = inorder[0:rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder + 1:]

    lenLeftSubtree = len(leftInorder)

    leftPreorder = pre[1:lenLeftSubtree + 1]
    rightPreorder = pre[lenLeftSubtree + 1:]

    leftChild = buildTreeFromPreIn(leftPreorder, leftInorder)
    rightChild = buildTreeFromPreIn(rightPreorder, rightInorder)

    root.left = leftChild
    root.right = rightChild
    return root


pre = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
root = buildTreeFromPreIn(pre, inorder)
printTreeDetailed(root)