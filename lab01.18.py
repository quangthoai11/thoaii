# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:40:02 2024

@author: Admin
"""

gio_mot = input("Nhập vào giờ thứ nhất (giờ,phút,giây): ")
gio_hai = input("Nhập vào giời thứ hai (giờ,phút,giây): ")
h1, p1, s1 = map(int, gio_mot.split(','))
h2, p2, s2 = map(int, gio_hai.split(','))
giay_mot = h1 * 3600 + p1 *60 + s1
giay_hai = h2 * 3600 + p2 *60 + s2
tong = giay_mot + giay_hai
hieu = giay_mot - giay_hai
gio_tong = tong // 3600
phut_tong = tong % 3600 // 60
giay_tong = tong % 60
gio_hieu = hieu // 3600
phut_hieu = hieu % 3600 // 60
giay_hieu = hieu % 60
print(f"Tổng hai giờ là: {gio_tong}giờ {phut_tong}phút {giay_tong}giây")
print(f"Tổng hai giờ là: {gio_hieu}giờ {phut_hieu}phút {giay_hieu}giây")