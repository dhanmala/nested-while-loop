i=1
while i<=7:
    j=1
    while j<=i:
        if i==1 or j==7*2 or j==1 or i==6-2  :
            print("*",end="")
        else:
            print("",end="")
        j=j+1
    print()
    i=i+1            