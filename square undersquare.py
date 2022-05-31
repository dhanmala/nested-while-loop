#square under square
i=1
while i<=5:
    j=1
    while j<=5:
        if i==1 or j==1 or i==5 or j==5 or i==4 or j==3-1 or j==i-1 or j==i*2-0 or j==i*2-1 or i==2 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
        j=j+1
    print()
    i=i+1        