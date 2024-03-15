import math
def euclid(x1,y1,x2,y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
def Manhat(x1,y1,x2,y2):
    return math.fabs(x2 - x1)+math.fabs(y2 - y1)
def Cosin(x1,y1,x2,y2):
    return 1-(x2 * x1+y2 * y1)/((x2**2 + y2**2)**0.5*(x1**2 + y1**2)**0.5)
print(euclid(2,1,3,4))
print(Cosin(2,1,3,4))
print(Manhat(2,1,3,4))