def multiplication(m,n):
    if n==1:
        return m
    if n<1:
        return
    smalloutput = multiplication(m,n-1)
    return m+smalloutput
from sys import setrecursionlimit
setrecursionlimit(11000)
m = int(input())
n = int(input())
print(multiplication(m,n))