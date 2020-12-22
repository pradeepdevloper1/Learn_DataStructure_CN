def issortedBetter(arr,si):
    l=len(arr)
    if si==l or si==l-1:
        return True
    if arr[si]>arr[si+1]:
        return False
    isSorted=issortedBetter(arr,si+1)
    return isSorted    

arr=[1,2,3,40,5,6,7]
print(issortedBetter(arr,0))