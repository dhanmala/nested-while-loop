i=1
while i<=3:
    j=1
    while j<=4:
        if i==1 or j==1 or i==1 or j==4 or j==6-i or j==i-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ") 
        j=j+1
    print()
    i=i+1           