n=int(input("enter the number of terms"))
x=int(input("enter the value of x"))
i=1
sum=0
while i<=n:
    sum=sum+((x**i)/i)
print(sum)   
i=i+1