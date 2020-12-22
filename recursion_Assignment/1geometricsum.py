def gs(k):
    if k==0:
        return 1
    return (1/(2**k))+gs(k-1)

n=int(input())
print(format(gs(n),'.5f'))
    