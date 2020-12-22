def Ispalirec(st,s,e):
    if s==e:
        return True
    if st[s]!=st[e]:
        return False
    if s<e+1:
        return Ispalirec(st,s+1,e-1)
    return True 

def isPalindrome(st):
    n=len(st)
    if n==0:
        return True
    return  Ispalirec(st,0,n-1)

st=input()
if(isPalindrome(st)):
    print("true")
else:
    print("false")    