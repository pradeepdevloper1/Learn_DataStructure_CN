def LastIndex(a,x):
    l=len(a)
    if l==0:
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
    


a=[1,3,7,9,9,7,8]
print(LastIndex(a,7))