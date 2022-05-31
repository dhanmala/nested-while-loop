n=int(input("enter the number of rows"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(j,end="")
        j=j-1
    print()
    i=i+1
    
