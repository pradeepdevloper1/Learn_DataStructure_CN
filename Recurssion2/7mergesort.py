def mergeSort(arr, start, end):
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L,0,mid-1)
 
        mergeSort(R,mid,len(arr))
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
