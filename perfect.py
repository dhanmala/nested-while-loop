i=2
sum=1
n=int(input("enter number"))
while (i<=n//2):
    if (n%i==0):
        sum+=1
        i+=1
if sum==n:
    print(n,"is not perfect number") 
else:
    print(n,"is a perfect number") 
