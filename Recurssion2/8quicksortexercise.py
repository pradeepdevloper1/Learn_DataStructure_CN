def partition(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if a[i] < pivot:
            c=c+1
    a[si],a[si+c]=a[si+c],a[si]
    pivot_index=si+c
    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>=pivot:
             j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return pivot_index   

def quickSort(arr, start, end):
    # Please add your code here
    if start>=end:
        return
    pivot_index=partition(arr,start,end)
    quickSort(arr,start,pivot_index-1)
    quickSort(arr,pivot_index+1,end)
    return arr
    

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
