def LastIndex(a,x,si):
    l=len(a)
    if si==l:
        return -1  
    smallerListOutput=LastIndex(a,x,si+1)
    if smallerListOutput !=-1:
        return smallerListOutput
    else:
        if a[si]==x:
            return si
        else:
            return -1 
    


a=[1,3,7,9,9,7,8]
print(LastIndex(a,7,0))