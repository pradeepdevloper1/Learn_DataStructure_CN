
def binarysearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    if a[mid] > x:
        return binarysearch(a,x,si,mid-1)
    else:
        return binarysearch(a,x,mid+1,ei)


a=[1,2,3,4,5,6,7,8,9,10]
print(binarysearch(a,4,0,9))    
