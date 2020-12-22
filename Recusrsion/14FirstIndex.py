def firstIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    smallerList=a[1:]
    smallerListOutput=firstIndex(smallerList,x)
    if smallerListOutput ==-1:
        return -1
    else:
        return smallerListOutput+1    


a=[1,3,7,9,9,7,8]
print(firstIndex(a,7))