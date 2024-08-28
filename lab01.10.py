# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:24:36 2024

@author: Admin
"""

so_xe = int(input("Nhập vào biển số xe (gồm 4 chữ số): "))
ngan_1 = so_xe // 1000
tram_1 = so_xe // 100 % 10
chuc_1 = so_xe // 10 % 10
don_vi_1 = so_xe % 10
tong_1 = ngan_1 + tram_1 + chuc_1 + don_vi_1

chuc_2 = tong_1 // 10
don_vi_2 = tong_1 % 10
tong_2 = chuc_2 + don_vi_2

chuc_3 = tong_2 // 10
don_vi_3 = tong_2 % 10
tong_3 = chuc_3 + don_vi_3
print(f"Biển số xe bạn được {tong_3} nút")  