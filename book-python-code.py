# from threading import *

# def dispaly():
#     for i in range(1,11):
#         print("child Thread")
# t = Thread(target = dispaly)

# t.start()
# for i in range(1,11):
#     print("main thread")

# from abc import*
# class Hello(ABC):
#     @abstractmethod
#     def hii(self):
#         print("hello")


# class Abc(Hello):
#     def hii(self):
#         return 10


# class Bcd(Hello):
#     def hii(self):
#         return 20

# t =Abc()
# print(t.hii())
# t2 = Bcd()
# print(t2.hii())



# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         return 30


# class Test2(Test):
#     def m1(self):
#         return 100

# t1 = Test2()
# print(t1.m1())


# import re

# pattern = re.compile("oo")
# matcher = pattern.finditer("this is a very good boy")
# for d in matcher:
#     if "oo" in d:
#         print("true")
#     else:
#         print("false")

# list1 = [10, 20, 4, 45, 99]

# list1.sort()
# print(list1[-2])

# def findDuplicate(x):
#     n = len(x)
#     repeated=[]
#     for i in range(n):
#         k = i+1
#         for j in range(k,n):
#             if x[i]==x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated

# lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# print(findDuplicate(lst))



# def findMissingNumber(x):
#     n = len(x)
#     sum = (n+1)*(n+2)//2
#     for i in range(n):
#         sum-=x[i]
#     return sum

# A = [1, 2, 4, 5, 6]
# miss = findMissingNumber(A)
# print(miss)

# def findFactorial(n):
#     if n < 0:
#         return n
#     elif  n==0 or n==1:
#         return 1
#     else:
#         fact = 1
#         while n >1:
#             fact*=n
#             n -=1
#             print(fact)
#         return fact

# n = 6
# print(findFactorial(n))


# def findMaxOccuresElement(x):

#     mx = 0
#     res = x[0]
#     for i in x:
#         freq = x.count(i)
#         if freq > mx:
#             mx = freq
#             res = i
#     return res

# s = [9, 4, 5, 4, 4, 5, 9, 5, 4,3,3,3,3,3,3,3] 
# print(findMaxOccuresElement(s))


# from collections import Counter

# def findDuplicateString(str):
#     wc = Counter(str)
#     print(wc)
#     j=-1
#     for i in wc.values():
#         j = j+1
#         if (i>1):
#             print(wc.keys()[j])


# str = "geeksforgeeks"
# findDuplicateString(str)

# def fact(n):
#     if n==0 or n ==1:
#         return 1
#     else:
#         return n*fact(n-1)

# n = 5
# print(fact(n))

def findFact(n):
    if n==1 or n==0:
        return 1
    else:
        fact =1
        while(n>1):
            fact*=n
            n -=1
        return fact
n = 400
print("ghgh",findFact(n))