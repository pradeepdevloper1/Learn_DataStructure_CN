# Problem: Remove x from string
def removeX(s):
    if len(s)==0:
        return s
    smallerlistoutput=removeX(s[1:])
    if s[0]=='x':
        return smallerlistoutput
    else:
        return s[0]+smallerlistoutput  
    pass

# Main
string = input()
print(removeX(string))
