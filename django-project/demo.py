

# def demo(arr,n):
#        left = 0
#        right = n-1
#        while left <right:
#               while arr[left]==0 and left < right:
#                   left+=1
#               while arr[right]==1 and left < right:
#                      right-=1

       
#               if  left < right:
#                      arr[left]=0
#                      arr[right]=1
#                      left+=1
#                      right-=1
#        return arr

# arr = [0, 1, 0, 1, 1, 1] 
# n = len(arr)
# print(demo(arr,n))


def seg(arr):

       res = ([x   for x in arr if x ==0] + [ x for x in arr if x==1])
       print(res)

arr = [0, 1, 0, 1, 1, 1] 

seg(arr)
              


