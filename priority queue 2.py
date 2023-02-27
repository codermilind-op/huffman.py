# def down_heapify(arr,i,n):
#     parentIndex=i
#     leftChildIndex=2*parentIndex+1
#     rightChildIndex=2*parentIndex+2
#
#     while leftChildIndex<n:
#         minIndex=parentIndex
#         if arr[minIndex]==arr[leftChildIndex]:
#             minIndex=leftChildIndex
#         if rightChildIndex<n and arr[minIndex]>arr[rightChildIndex]:
#             minIndex=rightChildIndex
#         if minIndex==parentIndex:
#             return
#         arr[minIndex],arr[parentIndex]=arr[parentIndex],arr[minIndex]
#         parentIndex=minIndex
#         leftChildIndex=2*parentIndex+1
#         rightChildIndex=2*parentIndex+2
#     return
#
# def heapsort(arr):
#     n=len(arr)
#     for i in range(n//2 -1,-1):
#         down_heapify(arr,i,n)
#
#     for i in range(n-1,0,-1):
#         arr[0],arr[i]=arr[i],arr[0]
#         down_heapify(arr,0,n)
#     return
#
# arr=[int(ele) for ele in input().split()]
# heapsort(arr)
# for ele in arr[::-1]:
#     print(ele,end=" ")

#
# def down_heapify(arr, i, n):
#     parentIndex = i
#     leftChildIndex = 2 * parentIndex + 1
#     rightChildIndex = 2 * parentIndex + 2
#
#     while leftChildIndex < n:
#         minIndex = parentIndex
#         if arr[minIndex] > arr[leftChildIndex]:
#             minIndex = leftChildIndex
#         if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
#             minIndex = rightChildIndex
#         if minIndex == parentIndex:
#             return
#         arr[minIndex], arr[parentIndex] = arr[parentIndex], arr[minIndex]
#         parentIndex = minIndex
#         leftChildIndex = 2 * parentIndex + 1
#         rightChildIndex = 2 * parentIndex + 2
#     return
#
#
# def heapSort(arr):
#     # Build the heap
#     n = len(arr)
#     for i in range(n // 2, -1, -1):
#         down_heapify(arr, i, n)
#
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         down_heapify(arr, 0, i)
#     return
#
#     # Removing n elements from the heap and put them at correct position
#
#
# arr = [int(ele) for ele in input().split()]
# heapSort(arr)
# for ele in arr[::-1]:
#     print(ele, end=" ")









#
# import heapq
#
# def kSmallest(arr,k):
#     heap=arr[:k]
#     heapq._heapify_max(heap)
#     n=len(arr)
#     for i in range(k,n):
#         if heap[0]>arr[i]:
#             heapq._heapreplace_max(heap,arr[i])
#     return heap
#
# n=int(input())
# lst=list(int(i) for i in input().strip().split(' '))
# k=int(input())
# ans=kSmallest(lst,k)
# ans.sort()
# print(*ans,sep='')


import heapq


def kSmallest(arr, k):
    heap = arr[:k]
    heapq._heapify_max(heap)
    n = len(arr)
    for i in range(k, n):
        if heap[0] > arr[i]:
            heapq._heapreplace_max(heap, arr[i])
    return heap


arr = [10, 6, 7, 2, 3, 8, 9, 11, 1]
k = 4
elements = kSmallest(arr, 4)
for ele in elements:
    print(ele, end=" ")