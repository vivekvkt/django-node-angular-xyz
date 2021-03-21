# def reverseStrSlice(str):
#     data = str[::-1]
#     return data

# str = "vivek"
# output = reverseStrSlice(str)
# print(output)


# def reverseStrForLoop(str):
#     s1  =  ''
#     for i in str:
#         s1=  i + s1
#     return s1
# str = "vivek"
# output = reverseStrForLoop(str)
# print("loop",output)

# def reverseStrWhileLoop(str):
#     s1 = ''
#     l1 = len(str)-1
#     while l1>=0:
#         s1+=str[l1]
#         l1-=1
#     return s1

# str = "vivek"
# output = reverseStrWhileLoop(str)
# print("whileloop","".join(output))

# def reverseStrRecursive(str):
#     if len(str)==0:
#         return str
#     else:
#         return reverseStrRecursive(str[1:]) + str[0]

# str = "vivek"
# print("recursive",reverseStrRecursive(str))


# reverse order of word in string

# def reverseWordStr(str):
#     s = str.split()
#     l1 = len(s)-1
#     lst = []
#     while l1>=0:
#         lst.append(s[l1])
#         l1-=1
#     output = " ".join(lst)
#     print("word",output)

# str = "hello vivek"
# reverseWordStr(str)


# def reverseWordStr(str):
#     s = str.split()
#     l1 = len(s)
#     print(l1)
#     lst = []
#     i=0
#     while i<l1:
#         print(i)
#         lst.append(s[i][::-1])
#         i= i+1
#     output = " ".join(lst)
#     print("word",output)

# str = "hello vivek"
# reverseWordStr(str)




# def find_duplicate_in_list(arr):
#     dup = []
#     for i in range(0, len(lst)-1):
#         if lst[i]==lst[i+1] and lst[i] not in dup:
#             dup.append(lst[i])
#     return dup

# lst  = [1,2,3,1,5,3,3,1,5,5]
# lst.sort()
# print(find_duplicate_in_list(lst))


# def find_duplicate_in_list(arr):
#     dup = []
#     for i in arr:
#         if i not in dup:
#             dup.append(i)
       
#     return dup

# lst  = [1,2,3,1,5,3,3,1,5,5]
# lst.sort()
# print(find_duplicate_in_list(lst))


# def findMissingElementInList(arr):
#     n = len(arr)
#     total = (n+1)*(n+2)//2
#     print(total)
#     for i in range(n):
#         total-=arr[i]
#     return total

# A = [1, 2, 4, 5, 6]
# print(findMissingElementInList(A))















