def IsSorted(a):
    l=len(a)
    if l==0 or l==1:
        return True
    if a[0]>a[1]:
        return False
    smallerList=a[1:]
    isSmallerListSorted=IsSorted(smallerList)
    if isSmallerListSorted:
        return True
    else :
        return False            

a=[]
print(IsSorted(a))        