# binary tree node
public class BinaryTreeNode<T> {

    public T data;
    public BinaryTreeNode<T> left;
    public BinaryTreeNode<T> right;

    public BinaryTreeNode(T data){
        this.data= data;
    }
}

# search node in bst


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data;
        self.left = None
        self.right = None


def search(root, x):
    if root == None:
        return False
    if root.data == x:
        return True
    elif root.data > x:
        return search(root.left, x)
    else:
        return search(root.left, x)


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


import queue


def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not (q.empty())):
        current_node = q.get()
        print("Enter left child of", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter right child of", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root


root = takeTreeInputLevelWise()
printTreeDetailed(root)
search(root, 5)

#
#
# print element in range k1 and k2
#
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def search(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    elif root.data>x:
        return search(root.left,x)
    else:
        return search(root.left,x)

def printBetweenK1K2(root,k1,k2):
    if root==None:
        return
    if root.data>k2:
        printBetweenK1K2(root.left,k1,k2)
    elif root.data<k1:
        printBetweenK1K2(root.right,k1,k2)
    else:
        print(root.data)
        printBetweenK1K2(root.left,k1,k2)
        printBetweenK1K2(root.right,k1,k2)

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

import queue
def takeTreeInputLevelWise():
    q=queue.Queue()
    print("Enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left child of",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        print("Enter right child of",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root

root=takeTreeInputLevelWise()
printTreeDetailed(root)
printBetweenK1K2(root,5,10)


#
#
#construct bst
#
import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# def constructBST(lst):
#############################
# PLEASE ADD YOUR CODE HERE #
#############################


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = int(input())
if (n > 0):
    lst = [int(i) for i in input().strip().split()]
else:
    lst = []
root = constructBST(lst)
preOrder(root)

#
#
#
# check is bst?


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def search(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    elif root.data>x:
        return search(root.left,x)
    else:
        return search(root.left,x)

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

import queue
def takeTreeInputLevelWise():
    q=queue.Queue()
    print("Enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left child of",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        print("Enter right child of",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root

def minTree(root):
    if root==None:
        return 100000
    leftMin=minTree(root.left)
    rightMin=minTree(root.right)
    return min(leftMin,rightMin,root.data)

def maxTree(root):
    if root==None:
        return -100000
    leftMax=maxTree(root.left)
    rightMax=maxTree(root.right)
    return max(leftMax,rightMax,root.data)

def isBST(root):
    if root==None:
        return True
    leftMax=maxTree(root.left)
    rightMin=minTree(root.right)
    if root.data>rightMin or root.data<=leftMax:
        return False
    isLeftBST=isBST(root.left)
    isRightBST=isBST(root.right)
    return isLeftBST and isRightBST

root=takeTreeInputLevelWise()
printTreeDetailed(root)
isBST(root)


#
#
#
# improved solution for check bst

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data;
        self.left = None
        self.right = None


def search(root, x):
    if root == None:
        return False
    if root.data == x:
        return True
    elif root.data > x:
        return search(root.left, x)
    else:
        return search(root.left, x)


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


import queue


def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not (q.empty())):
        current_node = q.get()
        print("Enter left child of", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter right child of", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root


def minTree(root):
    if root == None:
        return 100000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)


def maxTree(root):
    if root == None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.data)


def isBST2(root):
    if root == None:
        return 100000, -100000, True
    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    isTreeBST = True
    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False
    if not (isLeftBST) or not (isRightBST):
        isTreeBST = False

    return minimum, maximum, isTreeBST


root = takeTreeInputLevelWise()
printTreeDetailed(root)
isBST2(root)


#
#
#another solution for check bst
#
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data;
        self.left = None
        self.right = None


def search(root, x):
    if root == None:
        return False
    if root.data == x:
        return True
    elif root.data > x:
        return search(root.left, x)
    else:
        return search(root.left, x)


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


import queue


def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not (q.empty())):
        current_node = q.get()
        print("Enter left child of", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter right child of", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root


def minTree(root):
    if root == None:
        return 100000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)


def maxTree(root):
    if root == None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.data)


def isBST3(root, min_range, max_range):
    if root == None:
        return True
    if root.data < min_range or root.data > max_range:
        return False

    isLeftWithinConstraints = isBST3(root.left, min_range, root.data - 1)
    isRightWithinConstraints = isBST3(root.right, root.data, max_range)

    return isLeftWithinConstraints and isRightWithinConstraints


root = takeTreeInputLevelWise()
printTreeDetailed(root)
isBST3(root, -10000, 10000)