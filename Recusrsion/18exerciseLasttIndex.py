def LastIndex(a, x):
    if len(a) == 0:
        return -1
    smallerList=a[1:]     
    smallerListOutput=LastIndex(smallerList,x)
    if smallerListOutput !=-1:
        return smallerListOutput+1 
    else:
        if a[0]==x:
            return 0
        else:
            return -1 
    
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(LastIndex(arr, x))
