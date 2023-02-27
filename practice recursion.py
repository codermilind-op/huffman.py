# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
#
#
# def fact1(n):
#     if n == 0:
#         return 1
#     smallOutput = fact(n - 1)
#     return n * smalloutput
#
#
# def sum_n(n):
#     if n == 0:
#         return 0
#     smallOutput = sum_n(n - 1)
#     output = smallOutput + n
#     return output
# n = int(input())
# print(fact(n))
# print(sum_n(n))









# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
#
#
# def fact1(n):
#     if n == 0:
#         return 1
#     smallOutput = fact(n - 1)
#     return n * smalloutput
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
# def print_1_to_n(n):
#     if n == 0:
#         return
#     print_1_to_n(n - 1)
#     print(n)
#     return
#
#
# def print_n_to_1(n):
#     if n == 0:
#         return
#     print(n)
#     print_n_to_1(n - 1)
#
#
# n = int(input())
# print(fact(n))
# print(sum_n(n))
# print_n_to_1(n)



#
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
#
# def fact1(n):
#     if n==0:
#         return 1
#     smalloutput=fact(n-1)
#     return n*smalloutput
#
# def sum1(n):
#     if n==0:
#         return 1
#     sumofoutput=sum1(n-1)
#     output=sumofoutput +n
#     return output
#
# def print_1_to_n(n):
#     if n==0:
#         return 1
#     print_1_to_n(n-1)
#     print(n)
#     return
#
# def print_n_to_1(n):
#     if n==0:
#         return 1
#     print(n)
#     print_n_to_1(n-1)
#
# n = int(input())
# print(fact(n))
# print(sum1(n))
# print_n_to_1(n)

#
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     fib_n_1=fib(n-1)
#     fib_n_2=fib(n-2)
#     output=fib_n_1+fib_n_2
#     return output
#
# n=int(input())
# print(fib(n))

#
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
#
#
# def fact1(n):
#     if n == 0:
#         return 1
#     smalloutput = fact(n - 1)
#     return n * smalloutput
#
#
# import sys
#
# sys.setrecursionlimit(3000)
#
# n = int(input())
# print(fact(n))
#


def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def fact1(n):
    if n==0:
        return 1
    smalloutput= fact(n-1)
    return n*smalloutput

import sys

sys.setrecursionlimit(3000)

n=int(input())
print(fact(n))