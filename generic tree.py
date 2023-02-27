# generic tree node
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()

n1=TreeNode(5)
n2=TreeNode(2)
n3=TreeNode(9)
n4=TreeNode(8)
n5=TreeNode(17)
n6=TreeNode(15)
n7=TreeNode(1)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n3.children.append(n6)
n3.children.append(n7)

#
#
#print tree (recursively)
#
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def printTree(root):
    # TNot a base case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)


def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, ":", end=" ")
    for child in root.children:
        print(child.data, ",", end=" ")
    print()

    for child in root.children:
        printTreeDetailed(child)


n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(9)
n4 = TreeNode(8)
n5 = TreeNode(7)
n6 = TreeNode(15)
n7 = TreeNode(1)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n3.children.append(n6)
n3.children.append(n7)
printTreeDetailed(n1)


#
#
#take tree input(recursively)
#
#
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def printTree(root):
    # TNot a base case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)


def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    print()

    for child in root.children:
        printTreeDetailed(child)


def takeTreeInput():
    print('Enter Root Data')
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)

    print('Enter number of children for', rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root


root = takeTreeInput()
printTreeDetailed(root)



#
#
#
#number of nodes in numberic tree
#
#
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def printTree(root):
    # TNot a base case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)


def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ":", end="")
    print()

    for child in root.children:
        printTreeDetailed(child)


def takeTreeInput():
    print('Enter Root Data')
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)

    print('Enter number of children for', rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root


def numNodes(root):
    if root == None:
        return 0
    count = 1
    for child in root.children:
        count = count + numNodes(child)
    return count


root = takeTreeInput()
printTreeDetailed(root)
print(numNodes(root))


#
#
#
#
#tree input levelwise
#
#
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def printTree(root):
    # TNot a base case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)


def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    print()

    for child in root.children:
        printTreeDetailed(child)


def takeTreeInput():
    print('Enter Root Data')
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)

    print('Enter number of children for', rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root


import queue


def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    q.put(root)
    while (not (q.empty())):
        current_node = q.get()
        print("Enter num of children for", current_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print("Enter next child for", current_node.data)
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root


def numNodes(root):
    if root == None:
        return 0
    count = 1
    for child in root.children:
        count = count + numNodes(child)
    return count


root = takeTreeInputLevelWise()
printTreeDetailed(root)
print(numNodes(root))