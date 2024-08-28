# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:38:25 2024

@author: Admin
"""

a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
x = ((a + b) / (a ** (1/3) + b ** (1/3))) - ((a * b) ** (1 / 3))
y = (a ** (1/3) - b ** (1/3)) ** 2
t = x / y
print(f"Kết quả biểu thức là: {t}")