i=1
while i<=5:
    j=1
    while j<=5:
        if i==5 or j==5 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1            
