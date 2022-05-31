i=1
while i<=5:
    j=1
    while j<=5:
        if i==4 or j==4 or i==4-i:
            print("*",end="")
        else:
            print("",end="")
        j=j+1
    print()
    i=i+1      