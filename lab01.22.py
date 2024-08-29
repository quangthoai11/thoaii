# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:10:11 2024

@author: Admin
"""

a = float(input("Nhập vào giá trị của a: ")) 
b = float(input("Nhập vào giá trị của b: ")) 
p_t = f"Phương trình bậc nhất {a}x + {b} = 0"
if a == 0:
    if b == 0:
        print(f"{p_t} có vô số nghiệm")
    else:
        print(f"{p_t} vô nghiệm")
else:
    x = (-b) / a
    print(f"{p_t} có nghiệm x = {x}")