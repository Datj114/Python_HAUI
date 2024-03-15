def pt2(a,b,c):
    if(a==0):
        if b!=0:
            return f'phuong trinh co mot nghiem {-c/b}'
        return f'phuong trinh vo nghiem'
    denta=b**2-4*a*c
    if(denta>0):
        return f'phuong trinh co hai nghiem {(-b+denta**0.5)/2/a}, {(-b-denta**0.5)/2/a}'
    elif denta==0:
        return f'phuong trinh co nghiem kep {-b/2/a}'
    else:
        return f'phuong trinh vo nghiem'
print(pt2(1,2,-3))