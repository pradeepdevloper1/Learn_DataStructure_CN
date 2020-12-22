def firstIndexB(a,x,si):
    l=len(a)
    if si==l:
        return -1
    if a[si]==x:
        return si
    smallerListOutput=firstIndexB(a,x,si+1)
    return smallerListOutput   


a=[1,3,7,9,9,7,8]
print(firstIndexB(a,7,0))