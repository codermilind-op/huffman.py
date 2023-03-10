class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Hey!Stack is Empty!!")
            return
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Hey!Stack is Empty!!")
            return
        return self.__data[len(self.__data) - 1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size() == 0


s = Stack()
s.push(12)
s.push(13)
s.push(15)
while s.isEmpty() is False:
    print(s.pop())
s.top()



#
#
STACK USING LL
#
#
#
#
class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count + 1

    def pop(self):
        if self.isEmpty() is True:
            print("Hey!Stack is Empty!")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return data

    def top(self):
        if self.isEmpty() is True:
            print("Hey! Stack is Empty!")
            return
        data = self.__head.data
        return data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0


s = Stack()
s.push(12)
s.push(13)
s.push(15)
while s.isEmpty() is False:
    print(s.pop())
s.top()















