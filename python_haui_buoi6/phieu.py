class Product:
    def __init__(self,name,price,number) -> None:
        self.name=name
        self.price=price
        self.number=number
    def sum_price(self):
        return self.number*self.price
    def display(self):
        print(f'{self.name}   {self.price}   {self.number}      {self.sum_price()}')

id=input('id')
day=input('day')
id_ncc=input('idncc')
name_ncc=input('name_ncc')
add=input('add')
a=Product('tivi',30,2)
b=Product('quat',1.2,3)
c=Product('mobi',5,10)

print(f'----------phieu nhap hang------------')
print(f'ma phieu: {id}         ngay lap: {day}')
print(f'ma ncc: {id_ncc}         tenncc: {name_ncc}')
print(f'dia chi: {add}')
print(f'Tên hàng   Đơn giá   Số lượng   Thành tiền')
a.display()
b.display()
c.display()
print(f' tổng tiền: {a.sum_price()+b.sum_price()+c.sum_price()}')

