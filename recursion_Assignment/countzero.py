def countZeros(n):
    count = 0
    if n == 0:
        return 0

    b = countZeros(n//10)
    if n % 10 == 0:
        count = count + 1
        return count + b
    else:
        return count + b
    
    
n = int(input())
print(countZeros(n))