# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:12:29 2024

@author: Admin
"""

hinh = input("Nhập hình muốn tính chu vi (P) và diện tích (S) (vuông, chữ nhật, tròn): ")
if hinh == 'vuông':
    canh = float(input("Nhập độ dài cạnh (m): "))
    chu_vi = canh * 4
    dien_tich = canh ** 2
    print(f"Chu vi hình vuông là P = {chu_vi} m\nDiện tích hình vuông là S = {dien_tich} m\u00B2")
elif hinh == 'chữ nhật':
    dai = float(input("Nhập chiều dài (m): "))
    rong = float(input("Nhập chiều rộng (m): "))
    chu_vi = (dai + rong) * 2
    dien_tich = dai * rong
    print(f"Chu vi hình chữ nhật là P = {chu_vi} m\nDiện tích hình chữ nhật là S = {dien_tich} m\u00B2")
else:
    r = float(input("Nhập độ dài bán kính r (m): "))
    chu_vi = 2 * r * 3.14
    dien_tich = (r ** 2) * 3.14
    print(f"Chu vi hình tròn là P = {chu_vi} m\nDiện tích hình tròn là S = {dien_tich} m\u00B2")