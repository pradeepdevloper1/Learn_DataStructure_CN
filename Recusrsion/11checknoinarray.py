def checkNumber(arr, x):
    if len(arr)==0:
        return
    if arr[0]==x:
        return True
    else :
        smallarr=arr[1:]
        iffound=checkNumber(smallarr,x)
        if iffound:
            return True
        else:
            return False

    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
