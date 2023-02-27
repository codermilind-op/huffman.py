# class MapNode:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.next=None
#
# class Map:
#     def  __init__(self):
#         self.bucketSize=10
#         self.buckets=[None for i in range(self.bucketSize)]
#         self.count=0
#
#     def size(self):
#         return self.count
#
#     def getBucketIndex(self,hc):
#         return (abs(hc)%(self.bucketSize))
#
#     def insert(self,key,value):
#         hc=hash(key)
#         index =self.getBucketIndex(hc)
#         head=self.buckets[index]
#         while head is not None:
#             if head.key==key:
#                 head.value=value
#                 return
#             head=head.next
#         newNode=MapNode(key,value)
#         newNode.next=head
#         self.buckets[index]=newNode
#         self.count+=1
#
# m=Map()
# m.insert('milind',2)
# print(m.size())
# m.insert('millu',5)
# print(m.size())
# m.insert("milind",8)
# print(m.size())

#
#
#
#
# search and remove from the map
#
#
#
#
# class MapNode:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.next=None
#
# class Map:
#     def __init__(self):
#         self.bucketSize=10
#         self.buckets=[None for i in range(self.bucketSize)]
#         self.count=0
#
#     def size(self):
#         return self.count
#
#     def getBucketIndex(self,hc):
#         return(abs(hc)%self.bucketSize)
#
#     def getValue(self,key):
#         hc=hash(key)
#         index=self.getBucketIndex(hc)
#         head=self.buckets[index]
#         while head is not None:
#             if head.key==key:
#                 return head.value
#             head=head.next
#         return None
#
#     def remove(self,key):
#         hc=hash(key)
#         index=self.getBucketIndex(hc)
#         head=self.buckets[index]
#         prev=None
#         while head is not None:
#             if head.key==key:
#
#                 if prev is None:
#                     self.buckets[index]=head.next
#                 else:
#                     prev.next=head.next
#                 return head.value
#             prev=head
#             head=head.next
#
#     def insert(self,key,value):
#         hc=hash(key)
#         index=self.getBucketIndex(hc)
#         head=self.buckets[index]
#         while head is not None:
#             if head.key==key:
#                 head.value=value
#                 return
#             head=head.next
#         newNode=MapNode(key,value)
#         newNode.next=head
#         self.buckets[index]=newNode
#         self.count+=1
#
# m=Map()
# m.insert('Parikh',2)
# print(m.size())
# m.insert('Rohan',7)
# print(m.size())
# m.insert('Parikh',9)
# print(m.size())
# print(m.getValue('Rohan'))
# print(m.getValue('Parikh'))
# m.remove('Rohan')
# print(m.getValue('Rohan'))
# print(m.getValue('Parikh'))
#
#
#
#
#
#
#
#rehashing
#
#
#
# #
# class MapNode:
#     def __int__(self,key,value):
#         self.key=key
#         self.value=value
#         self.next=None
#
# class Map:
#
#     def __init__(self,key,value):
#         self.bucketSize=5
#         self.buckets=[None for i in range(self.bucketSize)
#                       ]
#         self.count=0
#
#     def size(self):
#         return self.count
#
#     def getBucketIndex(self,hc):
#         hc=hash(key)
#         index=self.getBucketIndex(hc)
#         head=self.buckets[index]
#         while head is not None:
#             if head.key==key:
#                 return head.value
#             head=head.next
#         return None
#
#     def remove(self,key):
#         hc=hash(key)
#         index=self.getBucketIndex(hc)
#         head=self.buckets[index]
#         prev=None
#         while head is not None:
#             if head.key==key:
#
#                 if prev is None:
#                     self.buckets[index]=head.next
#                 else:
#                     prev.next=head.next
#                 return head.value
#             prev=head
#             head=head.next
#         return None
#
#     def rehash(self):
#         temp=self.buckets
#         self.buckets=[None for i in range(2*self.bucketSize)]
#         self.bucketSize=2*self.bucketSize
#         self.count=0
#         for head in temp:
#             while head is not None:
#                 self.insert(head.key,head.value)
#                 head=head.next
#
#         def loadFactor(self):
#             return self.count / self.bucketSize
#
#         def insert(self, key, value):
#             hc = hash(key)
#             index = self.getBucketIndex(hc)
#             head = self.buckets[index]
#             while head is not None:
#                 if head.key == key:
#                     head.value = value
#                     return
#                 head = head.next
#             newNode = MapNode(key, value)
#             newNode.next = head
#             self.buckets[index] = newNode
#             self.count += 1
#             loadFactor = self.count / self.bucketSize
#             if loadFactor >= 0.7:
#                 self.rehash()
#
# m = Map()
# for i in range(10):
#      m.insert('abc' + str(i), i + 1)
#      print(m.loadFactor())
#
# for i in range(10):
#     print('abc' + str(i) + ':', m.getValue('abc' + str(i)))
#
# m.insert('Parikh',2)
# print(m.size())
# m.insert('Rohan',7)
# print(m.size())
# m.insert('Parikh',9)
# print(m.size())
# print(m.getValue('Rohan'))
# print(m.getValue('Parikh'))
# m.remove('Rohan')
# print(m.getValue('Rohan'))
# print(m.getValue('Parikh'))
#
# class MapNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# class Map:
#
#     def __init__(self):
#         self.bucketSize = 5
#         self.buckets = [None for i in range(self.bucketSize)]
#         self.count = 0
#
#     def size(self):
#         return self.count
#
#     def getBucketIndex(self, hc):
#         return (abs(hc) % (self.bucketSize))
#
#     def getValue(self, key):
#         hc = hash(key)
#         index = self.getBucketIndex(hc)
#         head = self.buckets[index]
#         while head is not None:
#             if head.key == key:
#                 return head.value
#             head = head.next
#         return None
#
#     def remove(self, key):
#         hc = hash(key)
#         index = self.getBucketIndex(hc)
#         head = self.buckets[index]
#         prev = None
#         while head is not None:
#             if head.key == key:
#
#                 if prev is None:
#                     self.buckets[index] = head.next
#                 else:
#                     prev.next = head.next
#                 return head.value
#             prev = head
#             head = head.next
#         return none
#
#     def rehash(self):
#         temp = self.buckets
#         self.buckets = [None for i in range(2 * self.bucketSize)]
#         self.bucketSize = 2 * self.bucketSize
#         self.count = 0
#         for head in temp:
#             while head is not None:
#                 self.insert(head.key, head.value)
#                 head = head.next
#
#     def loadFactor(self):
#         return self.count / self.bucketSize
#
#     def insert(self, key, value):
#         hc = hash(key)
#         index = self.getBucketIndex(hc)
#         head = self.buckets[index]
#         while head is not None:
#             if head.key == key:
#                 head.value = value
#                 return
#             head = head.next
#         newNode = MapNode(key, value)
#         newNode.next = head
#         self.buckets[index] = newNode
#         self.count += 1
#         loadFactor = self.count / self.bucketSize
#         if loadFactor >= 0.7:
#             self.rehash()
#
#
# m = Map()
# for i in range(10):
#     m.insert('abc' + str(i), i + 1)
#     print(m.loadFactor())
#
# for i in range(10):
#     print('abc' + str(i) + ':', m.getValue('abc' + str(i)))
#
#
# #     NICHE WALA CMNT FORM MAIN HI RAHEGA
#
# # m.insert('Parikh',2)
# # print(m.size())
# # m.insert('Rohan',7)
# # print(m.size())
# # m.insert('Parikh',9)
# # print(m.size())
# # print(m.getValue('Rohan'))
# # print(m.getValue('Parikh'))
# # m.remove('Rohan')
# # print(m.getValue('Rohan'))
# # print(m.getValue('Parikh'))
#
#
#
# class PriorityQueueNode:
#     def __init__(self, value, priority):
#         self.value = value
#         self.priority = priority
#
#
# class PriorityQueue:
#     def __init__(self):
#         self.pq = []
#
#     def getSize(self):
#         return len(self.pq)
#
#     def isEmpty(self):
#         return self.getSize() == 0
#
#     def getMin():
#         if self.isEmpty() is True:
#             return None
#         return self.pq[0].value
#
#     def __percolateUp(self):
#         childIndex = self.getSize() - 1
#         while childIndex > 0:
#             parentIndex = (childIndex - 1) // 2
#             if self.pq[childIndex].priority < self.pq[parentIndex].priority:
#                 self.pq[childIndex], self.pq[parentIndex] = self.pq[ParentIndex], self.pq[childIndex]
#                 childIndex = parentIndex
#             else:
#                 break
#
#     def insert(self, value, priority):
#         pqNode = PriorityQueueNode(value, priority)
#         self.pq.append(pqNode)
#         self.__percolateUp()
#
#     def removeMin(self):
#         pass


def heapSort(arr):
    n = len(arr)
# Build a maxheap. last parent will be at ((n//2)-1)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
# One by one extract the max elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=' ')











