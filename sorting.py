# from sys import stdin


# def sumOfTwoArrays(arr1, n, arr2, m, output):
#     i = n - 1
#     j = m - 1
#     carry = 0
#     k = max(n, m)
#     # k is the current index output array
#     while i >= 0 and j >= 0:
#         SUM = arr1[i] + arr2[j] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         i -= 1
#         j -= 1
#         k -= 1
#     while i >= 0:
#         SUM = arr1[i] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         i -= 1
#         k -= 1
#     while j >= 0:
#         SUM = arr2[j] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         j -= 1
#         k -= 1
#         output[0] = carry
#
#
# def takeInput():
#     n = int(input())
#     if n == 0:
#         return list(), 0
#     arr = list(map(int, input().rstrip().split(" ")))
#     return arr, n
#
#
# def printList(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()
#
#
# t = int(input().rstrip())
# while t > 0:
#     arr1, n = takeInput()
#     arr2, m = takeInput()
#     outputSize = (1 + max(n, m))
#     output = outputSize * [0]
#     sumOfTwoArrays(arr1, n, arr2, m, output)
#     printList(output, outputSize)
#
#     t -= 1

# from sys import stdin


# def sumOfTwoArrays(arr1, n, arr2, m, output):
#     i = n - 1
#     j = m - 1
#     carry = 0
#     k = max(n, m)
#     # k is the current index output array
#     while i >= 0 and j >= 0:
#         SUM = arr1[i] + arr2[j] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         i -= 1
#         j -= 1
#         k -= 1
#     while i >= 0:
#         SUM = arr1[i] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         i -= 1
#         k -= 1
#     while j >= 0:
#         SUM = arr2[j] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         j -= 1
#         k -= 1
#         output[0] = carry
#
#
# def takeInput():
#     n = int(input())
#     if n == 0:
#         return list(), 0
#     arr = list(map(int, input().rstrip().split(" ")))
#     return arr, n
#
#
# def printList(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()
#
#
# t = int(input().rstrip())
# while t > 0:
#     arr1, n = takeInput()
#     arr2, m = takeInput()
#     outputSize = (1 + max(n, m))
#     output = outputSize * [0]
#     sumOfTwoArrays(arr1, n, arr2, m, output)
#     printList(output, outputSize)
#
#     t -= 1

# s = "abcdef"
# print (s[4:2:-1])

#
# def arePermutation(str1, str2):
#     n1 = len(str1)
#     n2 = len(str2)
#     if (n1 != n2):
#         return False
#
#     # Sort both strings
#     a = sorted(str1)
#     str1 = ("".join(a))
#     b = sorted(str2)
#     str2 =( "".join(b))
#
#     # Compare sorted strings
#     for i in range(0, n1, 1):
#         if (str1[i] != str2[i]):
#             return False
#
#     return True
#
#
# str1 = input()
# str2 = input()
# if (arePermutation(str1, str2)):
#     print("true")
# else:
#     print("false")
# a = "abcdef" >= "abcd"
# print(a)

# def arePermutation(str1, str2):
#     # Get lengths of both strings
#     n1 = len(str1)
#     n2 = len(str2)
#
#     # If length of both strings is not same,
#     # then they cannot be Permutation
#     if (n1 != n2):
#         return False
#
#     # Sort both strings
#     a = sorted(str1)
#     str1 = " ".join(a)
#     b = sorted(str2)
#     str2 = " ".join(b)
#
#     # Compare sorted strings
#     for i in range(0, n1, 1):
#         if (str1[i] != str2[i]):
#             return False
#
#     return True
#
#
# # Driver Code
# if __name__ == '__main__':
#     str1 = input()
#     str2 = input()
#     if (arePermutation(str1, str2)):
#         print("true")
#     else:
#         print("false")

# string1 = input()
# string2 = input()

# If we create two lists out of these strings
# the lists will be different but if we create
# sets out of these strings we will get the same set

# list1 = list(string1)
# list2 = list(string2)
# print(list1)
# print(list2)
# # This will print False
# print(list1 == list2)
#
# set1 = set(string1)
# set2 = set(string2)
# print(set1)
# print(set2)
# # This will print True
# print(set1 == set2)

from sys import stdin

#
# def sumOfTwoArrays(arr1, n, arr2, m, output):
#     i = n - 1
#     j = m - 1
#     carry = 0
#     k = max(n, m)
#     # k is the current index output array
#     while i >= 0 and j >= 0:
#         SUM = arr1[i] + arr2[j] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         i -= 1
#         j -= 1
#         k -= 1
#     while i >= 0:
#         SUM = arr1[i] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         i -= 1
#         k -= 1
#     while j >= 0:
#         SUM = arr2[j] + carry
#         output[k] = SUM % 10
#         carry = SUM // 10
#         j -= 1
#         k -= 1
#         output[0] = carry
#
#
# def takeInput():
#     n = int(input())
#     if n == 0:
#         return list(), 0
#     arr = list(map(int, input().rstrip().split(" ")))
#     return arr, n
#
#
# def printList(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()
#
#
# t = int(input().rstrip())
# while t > 0:
#     arr1, n = takeInput()
#     arr2, m = takeInput()
#     outputSize = (1 + max(n, m))
#     output = outputSize * [0]
#     sumOfTwoArrays(arr1, n, arr2, m, output)
#     printList(output, outputSize)
#
#     t -= 1

# # In order to check if two strings are permuations
# # one solution is to convert each string into a set
# # and see if both produce the same set
#
# def checkPermSet(str1, str2):
#     return set(str1) == set(str2)
#
#
# # This will print true
# print(checkPermSet(string1, string2))
#
#
# # Another solution is count the number of occurrences
# # of each character in both strings, if the counts match
# # then the two strings are permutations.
#
# def checkPermDict(str1, str2):
#     # If the length is not the same
#     # then they are not permutations
#     if len(str1) != len(str2):
#         return False
#
#     # define dictionaries
#     dic1 = {}
#     dic2 = {}
#
#     # Initialize counts to 0
#     for c in str1:
#         dic1[c] = 0
#     for c in str2:
#         dic2[c] = 0
#
#     # Calcualte character counts
#     for c in str1:
#         dic1[c] += 1
#     for c in str2:
#         dic2[c] += 1
#
#     # Compare counts
#     for c, count in dic1.items():
#         # If there is a key or count mismatch
#         # then they are not permutations
#         if c not in dic2 or count != dic2[c]:
#             return False
#
#     # If we reach this point the two strings
#     # are permutations
#     return True
#
#
# # This will print True
# print(checkPermDict(string1, string2))
#
# def linear_search(c: "char", inp_str: str):
#
# 	# returns True if the passed character c is in the input string, otherwise returns False
#
# 	curr_index=0;
# 	length=len(inp_str);
#
# 	while curr_index<length:
# 		if inp_str[curr_index]==c:
# 			return True;
#
# 		curr_index+=1;
#
# 	return False;
#
#
# def check_perm(inp_str1: str, inp_str2: str):
#
# 	# determines whether input string 2 is a permutation of input string 1
# 	# runs linear search in input string 1 for every character in input string 2
#
# 	for each in inp_str2:
# 		if not linear_search(each, inp_str1):
# 			return False;
# 	return True;
#
# def main():
# 	print(check_perm("abc", ""));
#
# if __name__=="__main__":
# 	main();
#
# def switch_alt(inp_lst: list, length: int):
#
# 	curr_index=0;
# 	for each in range(length//2):
# 		inp_lst[curr_index], inp_lst[curr_index+1]=inp_lst[curr_index+1], inp_lst[curr_index];
# 		curr_index+=2;
#
# def main():
# 	lst=list(range(5));
# 	print(lst);
# 	switch_alt(lst);
# 	print(lst);
#
# if __name__=="__main__":
# 	main();

# def swap(list1):
#     n = 2 if len(list1)%2 == 0 else 3
#     for i in range(0,len(list1),n):
#         list1[i],list1[i+1] = list1[i+1], list1[i]
#     return list1
# listr = list(map(int,input().strip().split()))[:n]
# print(swap(listr))

# def linear_search(c: "char", inp_str: str):
#
# 	# returns True if the passed character c is in the input string, otherwise returns False
#
# 	curr_index=0;
# 	length=len(inp_str);
#
# 	while curr_index<length:
# 		if inp_str[curr_index]==c:
# 			return True;
#
# 		curr_index+=1;
#
# 	return False;
#
#
# def check_perm(inp_str1: str, inp_str2: str):
#
# 	# determines whether input string 2 is a permutation of input string 1
# 	# runs linear search in input string 1 for every character in input string 2
#
# 	for each in inp_str2:
# 		if not linear_search(each, inp_str1):
# 			return False;
# 	return True;
#
# print(check_perm("abc","bac"));

# li = [[1,2,3],[4,5,6],[7,8,9]]
# print(li[1][3])
#
# li = [[1,2,3,4],[5,6],[7,8,9]]
# print(li[2])

# li = [[1,2,3,4],[5,6],[7,8,9]]
# print(li[1][3])