# def func(a):
#     a = a + 10
#     return a
# a = 5
# func(a)
# print(a)

# def square(a):
#     ans  = a*a
#     return  ans
#
# a = 4
# a = square(a)
# print(a)
# a = 14
# def f():
#     a=12
# f()
# print(a)

# a=14
# def f():
#     global a
#     a=12
# f()
# print(a)
# a = 14
# def f():
#     a = 12
#     return a
# a = f()
# print(a)
# def function(a,b,c=1):
#     return a+b-c
# value = function(10,12)
# print(value)

# def function(a,b,c=1):
#     return a+b-c
# value = function(10,12,5)
# print(value)
# def function(a,b,c=1,d=5):
#     return a+b+c+d
# value = function(1,2,d=7)
# print(value)


# def wish(name,wish="Happy Birthday"):
#     print("Hello", name + ', ' + wish)
#     greet("Rohan")
#     greet("Hardik", "Happy New Year")


# n=int(input())
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(1,end="")
#     print("")

# n=int(input())
# i=1
# j=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(n+j+1, end='')
#         j=j+1
#     j=j-1; j=j-1;
#     print("*", end='' )
#     while j>=1:
#         print(n+j+1, end='' )
#         j=j-1
#     print("");
#     i=i+1

# n=int(input())
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(1,end="")
#     print("")
# n=int(input())
# i=1
# while i<=n :
#     j=1
#
#     while j<=n :
#
#         print(n-j+1, end="")
#
#         print("*", end='')
#
#         j=j+1
#
#     print()
#     i=i+1

n=int(input())
i=1
while (i<=n):
    j = n
    while(j>=1):
        if j!=i:
            print(j,end="",flush="true")
        else:
            print('*',end='',flush="true")
        j=j-1
    print("")
    i=i+1
