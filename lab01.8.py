# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:13:23 2024

@author: Student
"""

can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
BMI = can_nang / chieu_cao**2
print(f"chi so BMI cua ban la: {BMI:.2f}")