# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:41:42 2024

@author: Student
"""

N=int(input("Nhap so nguyen duong N co 2 chu so :"))
if N >= 10 and N <=99:
    hang_don_vi = N%10
    hang_chuc = N//10
Tong = hang_don_vi + hang_chuc
print("Tong cac chu so cua N la:", Tong)