# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:12:00 2024

@author: Admin
"""

a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(f"Thứ tự tăng dần các số là {a} {b} {c}")

N = input("Nhập vào 1 số nguyên N: ")
sap_xep = "".join(sorted(N))
print(f"Thứ tự tăng dần của dãy số là: {sap_xep}")