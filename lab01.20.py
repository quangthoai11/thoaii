# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:08:31 2024

@author: Admin
"""

a = float(input("Nhập vào số nguyên a: "))
b = float(input("Nhập vào số nguyên b: "))
c = float(input("Nhập vào số nguyên c: "))
if a > b:
    b = a
if b > c:
    c = b
print(f"Số lớn nhất là: {c}")