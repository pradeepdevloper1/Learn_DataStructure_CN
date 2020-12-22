def replaceChar(s,a,b):
    if len(s)==0:
        return s
    smallerlistoutput=replaceChar(s[1:],a,b)
    if s[0]==a:
        return b+smallerlistoutput
    else:
        return s[0]+smallerlistoutput        

arr='abcdxctctct'
print(replaceChar(arr,'c','x'))        