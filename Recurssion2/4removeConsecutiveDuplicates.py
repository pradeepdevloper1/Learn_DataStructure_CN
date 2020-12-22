def removeConsecutiveDuplicates(string):
    if len(string)<=1:
        return string
    soutput=removeConsecutiveDuplicates(string[1:])
    if string[0]==string[1]:
        return soutput
    else:
        return string[0]+soutput
        
    pass

s="xxxyyyzwwzzz"
print(removeConsecutiveDuplicates(s))