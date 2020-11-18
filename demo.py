
# n = int(input("enter the number:"))
# for i in range(1, n+1):
#     for j in range(1, n+1):
    #     print(n+1-j, end="")
    # print()
    
    
# n = int(input("enter the number :"))
# for i in range(1,n+1):
#     for j in range(0, i):
#         print(i, end=" ")
#     print()

#page no 367



# def reverse(arr, start,end):
#     while start < end:
#         arr[start],arr[end] = arr[end],arr[start]
#         start +=1
#         end -=1

# arr = [2,4,1,7]
# len1 = len(arr)-1
# print(len1)
# reverse(arr,0,len1)
# print(arr)

# def recursive(arr, start,end):
#     if start > end:
#         return
#     arr[start],arr[end] = arr[end],arr[start]
#     recursive(arr, start+1,end-1)

# arr = [2,4,1,7]
# len1 = len(arr)-1
# print(len1)
# recursive(arr,0,len1)
# print(arr)

# def getMissingNo(arr, n):
    
#     total = (n+1)*(n+2)//2
#     for  i in range(n):
#         total = total- arr[i]
#     return total
# arr = [1, 2, 4, 5, 6] 
# n = len(arr)
# miss = getMissingNo(arr,n) 
# print(miss)

#n = int(input("enter the number :"))


# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(j,end=" ")
#     print()

# for i in  range(1,n+1):
#     print(" "*(n-i), end="")
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()
    
# for i in range(0, n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(i-j, end="")
#     for k in range(0,i):
#         print(k, end= " ")
#     print()
# a = 10
# b = 20
# a = a+b
# b = a-b
# a = a-b
# print("aaaa",a)
# print("bbbb",b)



# b = [5,6,7,8] + [1,2,3,4]
# i = 10
# print type

# a = [ x  for x in range(1, 11) if x %2 ==0 else ]
# print(a)

# a = [ {"even":i } if i %2==0 else {"odd":i} for i in range(20)]
# print(a)

# list1 = [1,2,3,4,5,6]
# res = list(filter(lambda x:  (x> 3) ,list1))
# print(res)

# a = 10
# b = 10
# print(id(a))
# print(id(b))
# print(a is b)

# l = [10,20,"hello",10.4,40,90,30,70]
# print(l[1::3])

# t =(10,30,40,29)
# print(t)

# t1 = (20,10,40,50)
# print(t1)
# t1[0] = 90
# print(t1)


#page 72

# s = "vivek"

# i = len(s)-1

# t = ''
# while i>=0:
#     t = t +s[i]
#     i=i-1
# print(t)

# def reverse(str, start,end):
#     start = 0
#     end = len(str)-1
#     while start < end :
#         str[start],str[end] = str[end],str[start]
#         start = start+1
#         end = end-1
#     return str

# str = ["vivek", "hello"]
# reverse(str,0,1)
# print(' '.join(str))


# def reverseWord(str):
#     s2 = str.split()
#     l = len(s2)-1
#     list1 = []
#     i = 0
#     while i <= l:
#         list1.append(s2[i][::-1])
#         i = i + 1 
#     return ' '.join(list1) 
# str = "hello vivek"
# reverseWord(str)
# print(reverseWord(str))

# list1 = [0,1,2,3,4,5,6]

# list2 = []
# list3 = []
# for i in list1:
#     if i%2==0:
#         list2.append(i)
#     else:
#         if i%2!=0:
#             list3.append(i)
# print(list2)
# print(list3)
# d = {10:"vivek",20:"kumar"}
# d2 = {30:"yes",40:"no"}
# d.update(d2)
# print(d)
# from functools import reduce
# l = [10,20,30,40,50]
# res = reduce(lambda x,y:x-y,l)
# print(res)

# def common_element(a,b):
#     a_set = set(a)
#     b_set = set(b)
#     if (a_set | b_set):
#         print(a_set | b_set)
#     else:
#         print("no common element")
# a = [1,2,5,7,8,5]
# b = [2,1,7,10,4,20]
# common_element(a,b)


# def countX(lst,x):
#     count = 0
#     for i in lst:
#         if i == x:
#             count = count + 1
#     return count
    
# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
# x = 8
# countX(lst,x)
# print('{} has ocured {} times'.format(x,countX(lst,x)))

x = 10
y = 20

# x = x^y
# y = y^x
# x = x^y

# x = x+y
# y = x-y
# x = x-y

# print(x)
# print(y)

# import logging
# logging.basicConfig(filename='log.txt',level=logging.WARNING)
# print("Loggin module demo")
# logging.debug("this is debug")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical messi


# import pandas as pd
# import numpy as np

# list1 = ["geeks","hello","hiii"]
# data = pd.DataFrame(list1)

# dic2 = {"name":["vivek","KUMAR","tiwari"],"age":[30,19,30],"rollno":[30,19,30]}
# data2 = pd.DataFrame(dic2)
# data2['name'] = data2['name'].str.lower() 

# time = pd.date_range('26/2/2020', periods=10,freq='H')


# data3 = np.array(['g','e','e','k','s'])
# list1 = ['g','e','e','k','s']

# ser = pd.Series(list1)

# dictionary1 = {"hello":1,"boy":2,"hk":3}
# index = ['g','e','e','k','s','f','o']
# Data =[1, 3, 4, 5, 6, 2, 9]
# d = pd.Series(Data,index)
# data3 = pd.read_csv('employees.csv')
# new = data3['Gender'] != "Male"
# data3['new'] = new
# list1 = [1, 2, 3, 4 ,5, 6]
# list2 = [10, 9, 8, 7, 6, 5]

# a = np.array([[0 ,1 ,2],[3 ,4 ,5 ],
#               [6 ,7 ,8],[9 ,10 ,11]])
 
# a = 10
# b = 20
# a +=b

#num = int(input("Enter the number: "))
# if (num % 4 ==0 ):
#     if (num % 100==0):
#         if(num % 400 ==0 ):
#             print("{0} is a leap year:".format(num))
#         else:
#             print("{0} not leap year ".format(num))
#     else:
#         print("{0} is a leap year".format(num))

# else :
#     print("{0} is not leap year".format(num))
# lower = int(input("enter first no:"))
# high = int(input("enter second no :"))
# for num in range(lower, high+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i==0):
#                 #print("{0} is not prime no:".format(num))
#                 break;
#         else:
#             print("{0} is a prime no".format(num))

# num = int(input("enter the no:"))

# fact =1
# for i in range(1,num+1):
#     fact = fact * i
#     num = num-1
# print(fact)

# def fact(num):
#     if num==0:
#         return 1
    
#     else:
#         return num * fact(num-1)

# num = int(input("enter the number: "))
# fact(num)
# print(fact(num))
  
  
# num = int(input("enter the num:"))

# arm = 0
# temp = num  
# while temp > 0:
#     rem = temp % 10
#     arm  = arm+rem ** 3
#     temp = temp // 10

# if (num == arm):
#     print("arm strong nu")

# def bubblesort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j] ,arr[j+1] = arr[j+1],arr[j]
# arr = [64, 34, 25, 12, 22, 11, 90]

# bubblesort(arr)
# for i in range(len(arr)):
#     print(arr[i], end="  ")
# print()

# def count(arr, c):
#     res = 0
#     for i in range(len(arr)):
#         if(arr[i]==c):
#             res+=1
#     return res

# arr = "geeksforgeeks"
# c = 's'
# count(arr,c)
# print(count(arr,c))


# def removeDuplicate(num):
#     remove_list = []
#     for i in num:
#         if i not in remove_list:
#             remove_list.append(i)
#     return remove_list

# num = [2, 4, 10, 20, 5, 2, 20, 4] 
# print(removeDuplicate(num))


# def getMissing(arr,n):
#     n = len(arr)
#     total = (n+1)*(n+2)//2
#     for i in range(0,n):
#         total = total-arr[i]
#     return total
# arr = [1, 2, 4, 5, 6]
# n = len(arr)        
# res= getMissing(arr,n)
# print(res)
    
    
# def duplicate(arr, n1):
#     count = [0]*n1
#     print(" Repeating elements are ",end = " ")
#     for i in range(0,n1):
#         if (count[arr[i]]==1):
#             print(arr[i], end= ' ')
#         else:
#             count[arr[i]] = count[arr[i]] + 1
#     print()
# arr = [4, 2, 4, 5, 2, 3, 1] 
# n = len(arr)
# duplicate(arr,n)


# def reverseStr(str):
#     l = len(str)-1
#     rev = ''
#     while l>=0:
#         rev = rev + str[l]
#         l = l-1
#     return rev
# str = "vivek"

# print(reverseStr(str))

# def reveseword(str):
#     l1 = len(str)
#     s = str.split()
#     l2 = len(s)-1
#     rev = []
#     i=0
#     while i<=l2:
#         rev.append(s[i][::-1])
#         i +=1
#     #return rev
#     out = ' '.join(rev)
#     print(out)
# str = "Learning Python is very Easy"
# reveseword(str)

# def removeduplicate(str):
#     l = []
#     for x in str:
#         if x not in l:
#             l.append(x)
#     output = ''.join(l)
#     print(output)
# str = "geeksforgeeks"
# removeduplicate(str)

# def occuranceChar(str):
#     d = {}
#     for x in str:
#         if x in d.keys():
#             d[x] +=1
#         else:
#             d[x] = 1
#     print(d)
#     for k,v in d.items():
#         print("{}={} times".format(k,v))
# str = "geeksforgeeks"        
# occuranceChar(str)

# MAX_ASCII = 256

# def maxOccuringCharacter(str):
#     count =     [0] * MAX_ASCII
    
#     max = -1
#     c = ''
#     for i in str:
#         count[ord(i)]+=1
    
    
#     for i in str:
#         if max<count[ord(i)]:
#             max = count[ord(i)]
#             c = i
#     return c
# str = "geeksforgeeks"
# print(maxOccuringCharacter(str))

# x  = [1,2,3,4,5]
# y = [2,3,4,6]
# x = x+y
# print(x)

# def maxElemnt(arr,n):
    
#     # for i in range(1,n):
#     #     if arr[i] > max:
#     #         max  = arr[i]
#     return max(arr)

# arr = [20,10,49]
# n = len(arr)
# print(maxElemnt(arr,n))


# x = {"name":"vivek","age1":20}
# y = {"name":"yes","age":30}
# x.update(y)
# y.update(x)
# print(x)


# def fibnoci(n):
#     if n<0:
#         print("enter inccorrect no")
#     elif n == 0 :
#         return 1
    
#     a =0
#     b = 1
#     while n>2:
#         nth = a+b
#         a = b
#         b = nth
#         n = n -1
#         print(nth)
        
# n = 10
# fibnoci(n)

d1 = [1,2,3,4,5,6]
d2 = [2,3,4,5]
#d1.append(d2)
d1.extend(d2)
l2 = [1,9,2,3,4]
x = [i for i in l2]
a = 1
b = 2
a,b = b,a

# def reverseString(str):
#     str = str.split()
#     print(str)
#     len1 = len(str)
#     print(len1)
#     l1 = []
#     i = 0
#     while i < len1:
#         l1.append(str[i][::-1])
#         i +=1
#     output  = " ".join(l1)
#     print(output)
# str = "vivek kumar tiwari"
# reverseString(str)


# def reverseString(str):
#     str = str.split()
#     l1 = len(str)-1
#     l2 = []
#     while l1 >=0:
#         l2.append(str[l1])
#         l1 -=1
#     output = ' '.join(l2)
#     print(output)
# str = "vivek kumar tiwari"
# reverseString(str)


def  isAlphabet(x):
    return x.isalpha()
       
def reverse(str):
    LIST = toList(str)
    l = 0
    r = len(LIST)-1
    
    while l < r:
        if not isAlphabet(LIST[l]):
            l +=1
        elif not isAlphabet(LIST[r]):
            r -=1
        else:
            LIST[l],LIST[r] = swap(LIST[l],LIST[r])
            l+=1
            r-=1
    return toString(LIST)


def toList(str):
    l2 = []
    for i in str:
        l2.append(i)
    return l2

def toString(List):
    return ''.join(List)

def swap(a,b):
    return b, a


str1 = "a!!!b.c.d,e'f,ghi"
str = "v@vi$k"


l = [[1,3,6],[1,4,6],[1,3,7]]
result = []
for sublist in l:
    for item in sublist:
        result.append(item)

def reverse(str):
    i = len(str)-1
    rev = ' '
    while i >=0:
        rev = rev + str[i]
        i -=1
    return rev

str = "vivek"


def reverseRecursive(str):
    if len(str)==0:
        return str
    
    else:
        return reverseRecursive(str[1:]) + str[0]
    
str = "vivek"
            
            
def isAlphabet(s):
    return s.isalpha()
def reverseNotMovingSpecialCharacter(str):
    LIST = toList(str)
    l  = 0
    r = len(LIST)-1
    while l < r:
        if not isAlphabet(LIST[l]):
            l+=1
        elif not isAlphabet(LIST[r]):
            r-=1
        else:
            LIST[l],LIST[r] = swap(LIST[l],LIST[r])
            l+=1
            r-=1
    return toString(LIST)

def toList(str):
    l1 = []
    for i in str:
        l1.append(i)
    return l1

def toString(list):
    return  ' '.join(list) 
def swap(a,b):
    return b,a
str = "v@i#v!ek"



def reverseIterativestring(str):
    len1 = len(str)-1
    rev  = " "
    
    while len1 >=0:
        rev = rev + str[len1]
        len1 -=1
    return rev
str = "vivek"
#print(reverseIterativestring(str))


def reverseRecursive(str):
    if len(str)==0:
        return str
    else:
        return reverseRecursive(str[1:]) + str[0]
    
str = "vivek"
#print(reverseRecursive(str))


# def reverseInplaceWord(str):
#     str = str.split()
#     len1 = len(str)
#     list1 = []
#     i = 0
#     while i < len1:
#         list1.append(str[i][::-1])
#         i+=1
#     output = ' '.join(list1)
#     print(output)

# str = "vivek kumar tiwari"
# reverseInplaceWord(str)

# def reversestringWord(str):
#     str = str.split()
#     len1 = len(str)-1
#     l2 = []
#     while len1 >=0:
#         l2.append(str[len1])
#         len1 -=1
#     output = ' '.join(l2)
#     print(output)

# str = "vivek kumar tiwari"
# reversestringWord(str)

# def findSecondLargestElement(arr,n):
#     if n<2:
#         print("please enter invalid number")
#         return 
    
#     first = second = -1
#     for i in range(n):
#         if arr[i] > first:
#             second = first
#             first = arr[i]
#         elif(arr[i]>second and arr[i]!=first):
#             second = arr[i]
     
#     if second == -1:
#         print("element not second ")
#     else:
#         print("element number is second ", second)
# arr = [12,20]  
# n = len(arr) 
# findSecondLargestElement(arr,n)

# def maxelement(arr,n):
#     max = arr[0]
#     for i in range(1,n):
#         if arr[i]>max:
#             max = arr[i]
#     return max

# arr = [12,20]  
# n = len(arr)
# print(maxelement(arr,n))

# def findMissingElement(arr,n):
#     total = (n+1)*(n+2)//2
#     for i in range(n):
#         total = total-arr[i]
#     return total

# arr = [1, 2, 4,6, 3, 7, 8]
# n = len(arr)
# print(findMissingElement(arr,n))
        

# def findDuplicateElement(arr, n):
#     for i in range(n):
#         if arr[abs(arr[i])]>=0:
#             arr[abs(arr[i])] = -arr[abs(arr[i])]
#         else:
#             print(abs(arr[i]), end=' ')
#     print()
# arr = [1, 2, 3, 1, 3, 6, 6] 
# n = len(arr)
# findDuplicateElement(arr,n)


def uniqueElement(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = res ^ arr[i]
    return res

arr = [2, 3, 5, 4, 5, 3, 4]
n = len(arr)
a1 = 10
a2 = 10
print(a1 is a2)

# class Student:
    
#     x  = 10
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
        
#     def talk(self):
        
#         print(self.name)
#         print(self.age)
            
# obj = Student("vivek",30)

# obj.talk()




# class P:
#     a = 10
#     def __init__(self):
#         self.b = 20
# class C(P):
#     c = 30
#     def __init__(self):
#         super().__init__()
#         self.d  = 50


# dd = C()
# print(dd.b)


# class Person:
#     def __init__(self,name,age):
#         self.name  = name
#         self.age = age
    
#     def eatDrink(self):
#         print("eat drink")


# class Employees(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno = eno
#         self.esal = esal
        

#     def work(self):
#         print("python coding  is very easy")
        
#     def empInfo(self):
#         print(self.name)
#         print(self.age)

# e = Employees('vivek',48,2000,300)
# e.eatDrink()
# e.work()
# e.empInfo()
    
        
#single inheritance

# class A:
#     def m1(self):
#        # print("m1 method")
        
# class B(A):
#     def m1(self):
#         #print("m2 method")
#         super().m1()

# c = B()
# c.m1()

# multi level inheritance

# class A:
#     def m1(self):
#         print("m1 method")
# class B(A):
#     def m1(self):
#         print("m2 method")
# class C(B):
    
#     @classmethod
#     def m1(cls):
#         print("m3 method")
#         super(A,cls).m1(cls)

# d = C()



#hirarchle

# class A:
#     def m1(self):
#         print("m1 method")
# class B(A):
#     def m1(self):
#         print("m2 method")
# class C(A):
#     @classmethod
#     def m1(cls):
#         print("m3 method")
#         super(A,cls).m1(cls)
        

# d = C()
# print(d.m1())
#280 line 


# class A:
#     def __init__(self):
#         print("parant class constructor")
#     def m1(self):
#         print("parant instance method")

# class B(A):
#     @classmethod
#     def m2(cls):
#         super(B,cls).__init__(cls)
#         super(B,cls).m1(cls)
        
# B.m2()


# class A:
#     @staticmethod
#     def m1():
#         print("method m1")
# class B(A):
#     @staticmethod
#     def m2():
#         print("m2 method")
#         super(B,B).m1()
        

# B.m2()

# class Book:
#     def __init__(self,pages):
#         self.pages = pages
        
#     def __add__(self,other,t):
#        return self.pages + other.pages + t.pages


# b1 = Book(100)
# b2 = Book(400)
# b3 = Book(600)

# print(b1+b2+b3)
# class Test:
#     def m1(self):
#         print("m1 method")
#     def m1(self):
#         print("m2 method")
#     def m1(self):
#         print("m3 method")

# d = Test()
# d.m1()

# class Test:
#     def __init__(self,*a):
#         print("hello number of argument")


# t = Test(10)  
# t = Test(10,20)  
# t = Test(20,30)  
# t = Test(40,10)
# print(t)

# class Test:
#     def sum(self, **a):
#         sum = 0
#         for x in a:
#             sum +=x
#         print(sum)
        
# t1 = Test()
# t1.sum(10=20,20=30)
# t1.sum(30=20,20=40,10=60)


# class A:
#     def marry(self):
#         print("i am married with you")
#     def notMarry(self):
#         print("not married with you")

# class B(A):
#     def  marry(self):
#         print("again married with you")
#         super().marry()

#     def notMarry(self):
#         print("again not married with you")
       
# t = B()
# t.marry()

# class A:
#     def __init__(self,a,b):
#         self.name = a
#         self.dob = b
        
#     def display(self):
#         print(self.name)
#         print(self.dob)
        
        
# t = A('vivek',20)
# t.display()
# print(t.name)


# class A:
#     def __init__(self):
#         self.a = 10
#         self.b = 30
    
#     def dispaly(self):
#         print(self.a)
#         print(self.b)
        
# t = A()
# t.dispaly()
# t.a  = 2000
# t.b = 40000
# print(t.a,t.b)

# class Engine:
#     a = 10
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         print("engine specific functionality")
# class Car:
#     def __init__(self):
#         self.engine= Engine()
#     def m2(self):
#         print("Car using Engine car functionality")
#         print(self.engine.a)
#         print(self.engine.b)
# c = Car()
# c.m2()

# class P:
#     a = 10
#     def __init__(self):
#         self.b = 10
#     def m1(self):
#         print("hello m1 method")
#     @classmethod
#     def m2(cls):
#         print("parant class method")
    
#     @classmethod
#     def m3(cls):
#         print("m3 method functionality")


# class C(P):
#     pass
# c = C()
# print(c.a)
# c.m3()
# c.m2()
            
            
            
# class P:
#     a = 10
#     def __init__(self):
#         self.b = 20
# class C(P):
#     c = 30
#     def __init__(self):
#         super().__init__()
#         self.d = 30
        
# c = C()
# print(c.a)
# print(c.d)
# print(c.b)

# class A:
#     @classmethod
#     def m1(cls):
#         print("m1 method")
        
# class B(A):
#     def m1(self):
#         print("m2 method")
# class C(B):
#     def m1(self):
#         print("m3 method")
#         A.m1()

# s = C()
# s.m1()

# import numpy as np

# arr = np.array([[-1, 2, 0, 4],
#                 [4, -0.5, 6, 0],
#                 [2.6, 0, 7, 8],
#                 [3, -7, 4, 2.0]])



# a= np.array([[5,2,3],
#                  [4,2,7]])

# b = np.array([[1,10,3],
#                  [4,2,7]])

# c = np.sqrt(a)


# # import pandas as pd
# lst = ['geeks','for','geeks']

# df = pd.DataFrame(lst)


# data = {"Name":['tom','vivek','krish','akst'],
#         "age":[20,10,50,30],
#         "Address":['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         "Qualification":['Msc', 'MA', 'MCA', 'Phd']
#         }
# d1 = pd.DataFrame(data)


# data = pd.read_csv("nba.csv", index_col ="Name")


# row2 = data.iloc[2]

# import re
# count = 0
# pattern = re.compile("ab")
# matcher = pattern.finditer("ababababb")
# for match in matcher:
#     count+=1
#     print(match.start(),"...",match.end(),"...",match.group())
# print(count)


# import re,urllib
# import urllib.request
# u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
# text=u.read()
# numbers=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I)
# for n in numbers:
#     print(n)


# from threading import *
# def display():
#     for i in range(1,11):
#         print("child thread")
# t = Thread(target=display)
# t.start()
# for i in range(1,11):
#     print("Main thread")

# import mysql.connector
# try:
#     con=mysql.connector.connect(host='localhost',database='durgadb',user='root',password='root')
#     cursor=con.cursor()
#     cursor.execute(
#     "create table employees(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10))")
#     print("Table Created...")
#     sql = "insert into employees(eno, ename, esal, eaddr) VALUES(%s, %s, %s, %s)"
#     records=[(100,'Sachin',1000,'Mumbai'),
#     (200,'Dhoni',2000,'Ranchi'),
#     (300,'Kohli',3000,'Delhi')]
#     cursor.executemany(sql,records)
#     con.commit()
#     print("Records Inserted Successfully...")
#     cursor.execute("select * from employees")
#     data=cursor.fetchall()
#     for row in data:
#         print("Employee Number:",row[0])
#         print("Employee Name:",row[1])
#         print("Employee Salary:",row[2])
#         print("Employee Address:",row[3])
#         print()
#         print()
# except mysql.connector.DatabaseError as e:
#         if con:
#             con.rollback()
#             print("There is a problem with sql :",e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()


# try:
#     x = int(input("enter first Number: "))
#     y = int(input("enter first Number: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("cant divide with zero")
# except ValueError:
#     print("please provide int value only")
    
# finally:
#     print("this is the cleanup code")


# def reverse(str):
#     rev  = ''
#     for i in str:
#         rev = i + rev
#     return rev

# str = "geekforgeeks"


# def reverseString(str):
#     l = len(str)-1
#     rev  = ''
#     while l>=0:
#         rev = rev +str[l]
#         l = l -1 
#     return rev
# str = "geeksforgeeks"

        

#missing number

# def missingNumber(arr):
#     n = len(arr)
#     total = (n+1)*(n+2)//2
#     for i in range(n):
#         total = total-arr[i]
#     return total

# arr = [1, 2, 4, 6, 3, 7, 8]
# print(missingNumber(arr))

#find duplicte element

# def findDuplicateElement(arr,n):
#     for i in range(n):
#         if arr[abs(arr[i])]>0:
#             arr[abs(arr[i])] = - arr[abs(arr[i])]
#         else:
#             print(abs(arr[i]), end=" ")
#     print()
    
# arr = [1, 2, 3, 1, 3, 6, 6] 
# n = len(arr)
# findDuplicateElement(arr,n)

#find unique element

# def findUniqueElement(arr,n):
#     res = arr[0]
#     for i  in range(1,n):
#         res = res ^arr[i]
#     return res

# arr = [1, 2, 3, 1, 3, 6, 6] 
# n = len(arr)
# print(findUniqueElement(arr,n))
        
        
# import logging
# logging.basicConfig(filename='mylog.txt',level=logging.INFO)
# logging.info("A New request Came:")
# try:
#     x=int(input("Enter First Number: "))
#     y=int(input("Enter Second Number: "))
#     print(x/y)
# except ZeroDivisionError as msg:
#     print("cannot divide with zero")
#     logging.exception(msg)
# except ValueError as msg:
#     print("Enter only int values")
#     logging.exception(msg)
#     logging.info("Request Processing Completed")

# def check(s1,s2):
#     if (sorted(s1)== sorted(s2)):
#         print("anagrams")
#     else :
#         print("not anagrams")

# s1 = "bad"
# s2 = "dad"
# check(s1,s2)


# def missingElement(arr):
    
#     n = len(arr)
#     total = (n+1)*(n+2)//2
#     for i in range(n):
#         total = total-arr[i]
#     return total

# arr = [1, 2, 4,6, 3, 7, 8]

# print(missingElement(arr))

# def findDuplicate(arr):
#     n = len(arr)
#     for i in range(n):
#         if arr[abs(arr[i])]>0:
#             arr[abs(arr[i])] = - arr[abs(arr[i])]
#         else:
#             print(abs(arr[i]), end=" ")
            
#     print()

# arr = [1, 2, 3, 1, 3, 6, 6] 
# findDuplicate(arr) 


# class Engine:
#     a = 10
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         print("hello m1 method")
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#     def m2(self):
#         print("car using engine functionality")
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()
# c = Car()
# c.m2()

# class P:
#     a = 10
#     def __init__(self):
#         self.b  = 20
#     def m1(self):
#         print("hello m1 method")
#     @classmethod
#     def m2(cls):
#         print("parant class method")
#     @staticmethod
#     def m3():
#         print("parant class method")

# class C(P):
#     pass

# c = C()
# c.m1()
# c.m2()
# c.m3()
# print(c.a)


# class P:

#     a = 10
#     def __init__(self):
#         self.b = 20
# class C(P):
#     c = 30
#     def __init__(self):
#         super().__init__()
#         self.d = 40
# c1 = C()
# print(c1.a)
# print(c1.b)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print("name: ", self.name)
#         print("age: ", self.age)

# class Student(Person):
#     def __init__(self,name, age,rollno,marks):
#         super().__init__(name, age)
#         self.rollno = rollno
#         self.marks = marks
    
#     def display(self):
#         super().display()
#         print("ROllno: ",self.rollno)
#         print("marks: ",self.marks)
        
# s1 = Student("vivek",12,101,30)
# s1.display()


# class P:
#     a = 10
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         print("parant instance method")
#     @classmethod
#     def m2(cls):
#         print("parant class method")
#     @staticmethod
#     def m3():
#         print("static method")
        
# class C(P):
#     a = 999
#     def __init__(self):
#         self.b = 3000
#         super().__init__()
#         print(super().a)
    
#         super().m1()
#         super().m2()
#         super().m3()
        
# c = C()
# print(c.a)
        

# class A:
#     def m1(self):
#         print("A class method")
# class B(A):
#     def m1(self):
#         print("B class method")
# class C(B):
#     def m1(self):
#         print("C class method")
# class D(C):
#     def m1(self):
#         print("D class method")
# class E(D):
#     def m1(self):
#         print("E method ")
#         A.m1(self)
#         B.m1(self)
# e = E()
# e.m1()

# class A:
#     @staticmethod
#     def m1():
#         print("Parant  static method")
# class B(A):
#     @staticmethod
#     def m2():
#         super(B,B).m1()

# B.m2()


# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#     def __add__(self,other):
#         return self.pages + other.pages


# b1  = Book(100)
# b2 = Book(200)
# print(b1+b2)


# class Test:
#     def sum(self,*a):
#         total = 0
#         for x in a:
#             total = total +x
#         print(total)
# t = Test()
# t.sum(20)
# t.sum(30,40)



# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age

# class Employee(Person):
    
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno = eno
#         self.esal = esal
        
#     def dispaly(self):
#         print("name: ",self.name)
#         print("age :", self.age)
#         print("eno: ",self.eno)
#         print("sal:",self.esal)

# e1 = Employee('vivek',30,30,20)
# e1.dispaly() 


       
# x = 1
# def f(a):
#     x = a *a
    
#     return x 
# y = f(3)
# print(x,y)

# x = [0,1,[2]]
# x[2][0]=5
# x[2].append(4)
# print(x)

# names = ["a","b","c","d"]
# values = [1,2,3,4]
# for n,v in zip(names,values):
#     print(n,v)
                  
# a = [2,5,1,8,6]
# b=sorted(a)
# print(a)
# print(b)
# c = a.sort()

# a = (1,)
# print(type(a))
            
# a = {1,2,3,5,2}
# a.add(10)
# print(a)

# a = range(10)
# d = [ x for x in a if x %2 !=0]
# print(d)


x = [[1,2,3],[4,4,5],[0,2,1]]
y  =  [[1,2,3],[4,4,5],[0,2,1]]
res =  [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j] + y[i][j]
for d in res:
    print(d)

    
    
    
    





