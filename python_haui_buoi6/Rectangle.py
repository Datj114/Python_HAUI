class Rectangle:
    def __init__(self,wide,heigh) :
        self.wide = wide
        self.heigh=heigh
    def Perimeter(self):
        return (self.wide+self.heigh)*2
    def Area(self):
        return self.wide*self.heigh
    def display(self):
        print('chieu dai:',self.wide)
        print('chieu rong:',self.heigh)
        print('chu vi:',self.Perimeter())
        print('chieu dai:',self.Area())

r=Rectangle(4,5)
r.display()