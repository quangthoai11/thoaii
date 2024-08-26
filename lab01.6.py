# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:01:09 2024

@author: Student
"""

from datetime import datetime
namsinh=int(input("nhap nam sinh cua ban:"))
namhientai=datetime.now().year
tuoi=namhientai - namsinh
print(f"ban sinh nam {namsinh} vay ban tuoi {tuoi}")