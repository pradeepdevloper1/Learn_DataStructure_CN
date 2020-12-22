def firstIndex(arr, x,si):
    if len(arr) == si:
        return -1
    if arr[si] == x:
        return si
    ans = firstIndex(arr,x,si+1)
    if ans == -1:
        return -1
    else:
        return ans
    
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,0))
