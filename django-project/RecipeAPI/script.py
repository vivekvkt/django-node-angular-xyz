#!/usr/bin/env python

list1 = [2,3,20,["vivek"],'hello',[30,40,50,10]]


my_list = ['p','r','o','g','r','a','m','i','z']


data = ''.join(my_list)


data1 = tuple(my_list)

data2 = set(my_list)

my_list.append([4,7])

my_list.extend([4,7])

short = [4,2]
dd = my_list+ short

mylist = [[1,2,3],[4,5,6],[8,5,3]]

# for x in mylist:
#     if len(x)== 3:
#         print(x)
#         print(x[0])
# print(mylist[0])

datalist = [1,2,3,4,5,6]

for i, val in enumerate(datalist):    
    pass
names1 = ['Amir','Bear','Charlton','Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[0] = 'Bob'

sum = 0 
for ls in (names1, names2, names3):
    if ls[0]=='Alice':
        sum+=1
    if ls[0]=='Bob':
        sum+=9

        
test = "hello#vivek"
test2 = test.split('#')
values = [[3, 4, 5, 1], [33, 6, 1, 2]]


# x = 20.5
# y = 2.0
# print(x//y) 
#page 48  


# s1 = 'vivek'

# s2 = 'vivek1'
# if id(s1)==id(s2):
#     print("true")
# else:
#     print("false")

# str = "hello vivek"
# str1 = str.split()
# len1 = len(str1)-1
# list1 = []
# while len1 >=0:
#     list1.append(str1[len1])
    
#     len1 -=1
# output = ' '.join(list1)
# print(output)

# str = "hello vivek"
# str1 = str.split()
# len1 = len(str1)-1
# list1 = []
# d = 0
# while d <= len1:
#     list1.append(str1[d][::-1])
    
#     d += 1
# output = ' '.join(list1)
# print(output)

# s1 = "aceg"
# s2 = "bdfh"
# l1 = len(s1)
# l2 = len(s2)
# i, j=0,0
# output = ""
# while i< l1 or j < l2:
#     if i <= l1:
#         output +=s1[i]
#         i+=1
#     if j <= l2:
#         output +=s2[j]
#         j+=1
        
# print(output)


x = [ 2**i for i in range(1,10)]
x1 = ("hello",)

d = {}
d[10]="vivek"
d['hello']="ok"
d[10]="no"


d = {10:"vivek",20:"hello"}
x = {1:"no",2:'yes'}

a = d.update(x)


# word = "hello how are helo"

# dic1 = {}

# for d in  word:
#     if d in dic1:
#         dic1[d] = dic1.get(d,0)+1
#     else:
#         dic1[d] = 1
# print(dic1)

# Python code to merge dict using update() method 
# def Merge(dict1, dict2): 
#     res = {**dict1,**dict2} 
#     return res
      
# # Driver code 
# dict1 = {'a': 10, 'b': 8} 
# dict2 = {'d': 6, 'c': 4} 
  
# # This return None 
# d3 = Merge(dict1,dict2)
  
# # changes made in dict2 
# print(d3)


# from collections import  Counter

# str = "hello how are oyu hello"
# out  = Counter(str)
# print(out)

# d1 ={"john":20,"peter":10}
# d2 = {"john":455,"peter":10},
# a = {1:'a',2:'b',3:'c'}
# print(a.get(7,10))

a = {}
a[1] = 1
a['1'] = 2

a[1]=a[1]+1
print(a)
count = 0
for i in a:
    count += a[i]
print(count)


        
    


