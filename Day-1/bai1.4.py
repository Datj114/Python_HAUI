n=int(input())
x=float(input())
if(n%2==0):
    s=2016*x
    for i in range(2,n+1):
       s +=x**i/3**(i-1)

else:
    s=0
print(s)