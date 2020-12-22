def tower_hanoi(n,a,b,c):
    if n==1:
        print("Move 1st disk from",a,"to",c)
        return
    tower_hanoi(n-1,a,c,b)
    print("Move ",n,"th Disk From ",a,"to",c)
    tower_hanoi(n-1,b,a,c)

tower_hanoi(3,"s","h","d")        