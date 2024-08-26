# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:17:29 2024

@author: Student
"""

a=int(input("Nhap so nguyen a:"))
b=int(input("Nhap so nguyen b:"))
tong = a+b
hieu = a-b
tich = a*b
if b!=0:
    thuong_2cs=round(a / b , 2)
    thuong_3cs=round(a / b , 3)
    chia_lay_du=a%b
    chia_lay_nguyen=a//b
    print(f"Tong: {tong}")
    print(f"Hieu: {hieu}")
    print(f"Tich: {tich}")
    print(f"Thuong (lam tron 2 chu so): {thuong_2cs}")
    print(f"Thuong (lam tron 3 chu so): {thuong_3cs}")
    print(f"Chia lay du: {chia_lay_du}")
    print(f"chia lay nguyen: {chia_lay_nguyen}")
else :
    print ("Khong the chia cho 0")