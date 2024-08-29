# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:11:42 2024

@author: Admin
"""

char = input("Nhập vào một chữ cái hoa hoặc thường: ")
if char.islower():
    chu_hoa = char.upper()
    print(f"{char} là chữ thường đổi thành chữ hoa: {chu_hoa}")
else:
    chu_thuong = char.lower()
    print(f"{char} là chữ hoa đổi thành chữ thường: {chu_thuong}")