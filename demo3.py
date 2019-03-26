for m in range(1,10):
    print(" "*(9-m),m,end ="")
    for i in range(m, 1, -1):
        print(i-1,end="")
    for j in range(1,m):
        print(j+1,end="")
    print()
    