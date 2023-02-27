class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,end=':')
    if root.left !=None:
        print("L" ,root.left.data, end="," )
    if root.right != None:
        print("R", root.left.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(2)
btn3=BinaryTreeNode(3)
btn4=BinaryTreeNode(4)
btn5=BinaryTreeNode(5)

btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5

printTreeDetailed(btn1)









class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(2)
btn3=BinaryTreeNode(3)
btn4=BinaryTreeNode(4)
btn5=BinaryTreeNode(5)

btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5

printTreeDetailed(btn1)













#
# input in binary tree
#


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None
    root =BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

root= treeInput()
printTreeDetailed(root)




#
# nodes of binary tree
#


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def numNodes(root):
    if root==None:
        return 0
    leftCount=numNodes(root.left)
    rightCount=numNodes(root.right)
    return leftCount+rightCount+1

root=treeInput()
printTreeDetailed(root)
print(numNodes(root))






# node with largest data


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def largestData(root):
    if root==None:
        return -1 #ideally return -inf
    leftLargest=largestData(root.left)
    rightLargest=largestData(root.right)
    largest=max(leftLargest,rightLargest,root.data)
    return largest

root=treeInput()
printTreeDetailed(root)
largestData(root)



#
#
#
# number of leaf node
#
#

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def numLeafNode(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    numLeafLeft=numLeafNode(root.left)
    numLeafRight=numLeafNode(root.right)
    return numLeafRight+numLeafLeft

root=treeInput()
printTreeDetailed(root)
print(numLeafNode(root))