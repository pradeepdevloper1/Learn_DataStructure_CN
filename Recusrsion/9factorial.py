import sys 
sys.setrecursionlimit(3000) 

def fact(n):
    if n==0:
        return 1
    smalloutput=fact(n-1)
    return n*smalloutput    

n=int(input())
print(fact(n))    