# def fact1(n):
#     if n == 0:
#         return 1
#     smallOutput = fact(n - 1)
#     return n * smalloutput
#
#
# # for i in range(n):
# #     pow = pow * x
#
#     # return pow
#
#
# def sum_n(n):
#     if n == 0:
#         return 0
#     smallOutput = sum_n(n - 1)
#     output = smallOutput + n
#     return output
#
#
# # for i in range(n):
# #     pow = pow * x
#
#
# n = int(input())
# print(fact(n))
# print(sum_n(n))

# def power(x, n):
#     # initialize result by 1
#     pow = 1
#
#     # Multiply x for n times
#     for i in range(n):
#         pow = pow * x
#
#     return pow
#
#
# # Driver code
# if __name__ == '__main__':
#     x = int(input())
#     n = int(input())
#
#     # Function call
#     print(power(x,n))

# def func(num):
#     return func(num-1)
# num = 5
# ans = func(num-1)
# print(ans)
#
# def printNumbers(n):
#     if(n<0):
#         return
#     print(n,end=" ")
#     printNumbers(n-2)
# num = 5
# printNumbers(num)

# def fun(n):
#     if(n == 4):
#         return n
#     else:
#         return 2*fun(n+1)
#
#
# print(fun(2))
#
# def sumArray(arr):
#     print(type(arr))
#     print(arr)
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + sumArray(arr[1:])
#
#
# from sys import setrecursionlimit
#
# setrecursionlimit(11000)
# n = int(input())
# arr = list(int(i) for i in input().strip().split(' '))
# print(sumArray(arr))
# print(arr)

# def sumArray(a):
#     n = len(a)
#     if n == 1:  # base case
#         return a[0]
#
#     smallerOutput = a[1:]
#     output = a[0] + sumArray(smallerOutput)
#     return output
#
#
# # a = [1, 2, 3, 4, 5, 6]
# a=int(input())
# print(sumArray(a))1



count=0
def count_digit(num):
    global count
    if (num >0):
        if(num%10==0):
            count +=1
        count_digit(num // 10)
    return count
n=int(input())
print(count_digit(n))

#
# def countZero(n):
#     if n == 0:
#         return 1
#
#     if n == 1:
#         return 0
#
#     if n // 10 == 0:
#         return 0
#
#     smallList = countZero(n // 10)
#     print(smallList)
#     if n % 10 == 0:
#         return smallList + 1
#     else:
#         return smallList
#
#
# print(countZero())
