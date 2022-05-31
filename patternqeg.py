num=int(input("enter the number"))
i=0
while i<=num:
    j=0
    while j<=num:
        if (i==0) or (i==num-1) or (j==0)or (j==6-i):
            print("*",end="")
        else:
            print(" ",end="") 
        j=j+1
    print()
    i=i+1               