a=int(input("enter the number"))
i=1
while i<=a:
    j=1
    while j<=5:
        if j<=i:
            print(i,end="")
        else:
            print(j,end="") 
        j=j+1
    print()
    i=i+1       