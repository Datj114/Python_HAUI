n=int(input())
while n<0 or n>10000:
    n=int(input())
arr =[]
i=-1
while n/10!=0:
    arr.append(n%10)
    x= n%10
    n=n//10
    i+=1
    
if(i==3):
    print(f'{arr[i]} ngan {arr[i-1]} tram {arr[i-2]} chuc {arr[i-3]} don vi ')
elif (i==2):
    print(f'{arr[i-1]} tram {arr[i-2]} chuc {arr[i-3]} don vi ')
elif i==1:
    print(f' {arr[i-2]} chuc {arr[i-3]} don vi ')
else:
    print(f'{arr[i-3]} don vi ')



# cach 2


