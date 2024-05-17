import math
class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def __str__(self) -> str:
        print(f'diem co toa do x= {self.x}, y={self.y}')
def distance(A,B):
    return math.sqrt((A.x-B.x)**2+(A.y-B.y)**2)
class circle:
    def __init__(self,O,r) -> None:
        self.O=O
        self.r=r
    def Area(self):
        return math.pi*self.r**2
    def Perimeter(self):
        return 2*math.pi*self.r
    def testBelongs(self,A):
        if(distance(A,self.O)==self.r):
            print(f'diem thuoc duong tron')
        else:
            print(f'diem khong thuoc')
O=Point(0,0)
A=Point(0,5)
B=Point(0,4)
c=circle(O,5)
print(f'dien tich {c.Area()}, chu vi {c.Perimeter()}')
c.testBelongs(A)
c.testBelongs(B)