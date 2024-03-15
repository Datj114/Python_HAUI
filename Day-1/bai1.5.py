n=int(input())
while (n)<0 or (n)>1000000:
    n=int(input())
def Reversed(n):
    # x=''.join(reversed(n))
    reversed_text = ""
    for char in str(n):
        reversed_text = char + reversed_text
    return reversed_text
def isPrime(n):
    if n<3:
        return False
    for i in range(2,int(n**0.5)+1):
        if i%2==0:
            return False
    return True
if(isPrime((n)) and str(n)==Reversed(n)):
    print ('hop le')
else:
    print('khong hop le')