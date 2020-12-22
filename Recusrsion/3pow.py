def pow(base,exp):
    if exp==0:
        return 1
    if exp==1:
        return base    
    return base*pow(base,exp-1)    


x, y = input().split()
base=int(x)
exp=int(y)
print(pow(base,exp))